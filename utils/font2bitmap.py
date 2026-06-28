#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Needs freetype-py>=1.0 y PIL/Pillow

import sys
import shlex
import argparse
import bisect
import freetype
from PIL import Image, ImageDraw, ImageFont
import os


def to_int(string):
    """ Return integer value from a hex or decimal string"""
    return int(string, base=16) if string.startswith("0x") else int(string)


def get_chars(string):
    """ Return string comprised of given characters or range(s) of characters"""
    return ''.join(chr(b) for a in [
            (lambda sub: range(sub[0], sub[-1] + 1))
            (list(map(to_int, ele.split('-'))))
            for ele in string.split(',')] for b in a)


def wrap_str(string, items_per_line=32):
    """ Return a string wrapped to items_per_line with special care for escape characters"""
    length = len(string)
    lines = []
    i = 0
    end = 0
    while length > end:
        end = min(i + items_per_line, length)
        if string[end - 1] == '\\':
            end -= 2
        lines.append(string[i : end])
        i = end
    return "(\n    '" + "'\n    '".join(lines) + "'\n)"


def wrap_bytes(lst, items_per_line=16):
    """Return a string of items wrapped to items_per_line"""
    lines = [
        "".join(f'\\x{x:02x}' for x in lst[i : i + items_per_line])
        for i in range(0, len(lst), items_per_line)
    ]
    return "    b'" + "'\\\n    b'".join(lines) + "'"


def wrap_longs(lst, items_per_line=16):
    """Return a string of longs wrapped to items_per_line"""
    lines = [
        "".join(f'\\x{x:02x}' for x in lst[i : i + items_per_line])
        for i in range(0, len(lst), items_per_line)
    ]
    return "    b'" + "'\\\n    b'".join(lines) + "'"


class Bitmap():
    def __init__(self, width, height, pixels=None):
        self.width = int(width)
        self.height = int(height)
        self.pixels = pixels or bytearray(width * height)

    def bit_string(self):
        bits = ''
        for y in range(self.height):
            for x in range(self.width):
                bits += '1' if self.pixels[y * self.width + x] else '0'
        return bits

    def bitblt(self, src, x, y):
        srcpixel = 0
        dstpixel = y * self.width + x
        row_offset = self.width - src.width

        for _ in range(src.height):
            for _ in range(src.width):
                self.pixels[dstpixel] = (
                    self.pixels[dstpixel] or src.pixels[srcpixel])
                srcpixel += 1
                dstpixel += 1
            dstpixel += row_offset


class Glyph():
    def __init__(self, pixels, width, height, top, left, advance_width):
        self.bitmap = Bitmap(width, height, pixels)
        self.top = top
        self.left = left
        self.descent = max(0, self.height - self.top)
        self.ascent = max(0, max(self.top, self.height) - self.descent)
        self.advance_width = advance_width

    @property
    def width(self):
        return self.bitmap.width

    @property
    def height(self):
        return self.bitmap.height

    @staticmethod
    def from_glyphslot(slot):
        pixels = Glyph.unpack_mono_bitmap(slot.bitmap)
        width, height = slot.bitmap.width, slot.bitmap.rows
        top = slot.bitmap_top
        left = slot.bitmap_left
        advance_width = slot.advance.x // 64
        return Glyph(pixels, width, height, top, left, advance_width)

    @staticmethod
    def unpack_mono_bitmap(bitmap):
        data = bytearray(bitmap.rows * bitmap.width)
        for y in range(bitmap.rows):
            for byte_index in range(bitmap.pitch):
                byte_value = bitmap.buffer[y * bitmap.pitch + byte_index]
                num_bits_done = byte_index * 8
                rowstart = y * bitmap.width + byte_index * 8
                for bit_index in range(min(8, bitmap.width - num_bits_done)):
                    bit = byte_value & (1 << (7 - bit_index))
                    data[rowstart + bit_index] = 1 if bit else 0
        return data


class Font():
    def __init__(self, filename, width, height):
        self.face = freetype.Face(filename)
        self.face.set_pixel_sizes(width, height)
        self.font_filename = filename
        self.font_size = height

    def glyph_for_character(self, char):
        self.face.load_char(
            char, freetype.FT_LOAD_RENDER | freetype.FT_LOAD_TARGET_MONO)
        return Glyph.from_glyphslot(self.face.glyph)

    def get_valid_characters(self, text):
        """
        Return only characters that have valid glyphs in the font.
        The space character (32) is always considered valid even if it has no pixels.
        """
        valid = []
        invalid_count = 0
        
        for char in text:
            # Space is always valid (even though it has no pixels)
            if ord(char) == 32:
                valid.append(char)
                continue
                
            try:
                # Get the glyph index - if it's 0, it's the .notdef glyph
                glyph_index = self.face.get_char_index(ord(char))
                
                if glyph_index != 0:
                    # Render to check if it has pixels
                    self.face.load_char(char, freetype.FT_LOAD_RENDER | freetype.FT_LOAD_TARGET_MONO)
                    glyph = Glyph.from_glyphslot(self.face.glyph)
                    
                    # Check if the glyph has any actual pixels
                    has_pixels = False
                    for i in range(glyph.height):
                        for j in range(glyph.width):
                            if glyph.bitmap.pixels[i * glyph.width + j]:
                                has_pixels = True
                                break
                        if has_pixels:
                            break
                    
                    if has_pixels:
                        valid.append(char)
                    else:
                        invalid_count += 1
                else:
                    invalid_count += 1
            except:
                invalid_count += 1
                continue
        
        print(f"Filtered out {invalid_count} invalid characters")
        return ''.join(valid)

    def text_dimensions(self, text):
        width = 0
        max_ascent = 0
        max_descent = 0

        for char in text:
            glyph = self.glyph_for_character(char)
            max_ascent = max(max_ascent, glyph.ascent)
            max_descent = max(max_descent, glyph.descent)

            if glyph.left >= 0:
                char_width = int(
                    max(glyph.advance_width, glyph.width + glyph.left))
            else:
                char_width = int(
                    max(glyph.advance_width - glyph.left, glyph.width))
            width += char_width

        height = max_ascent + max_descent
        return (width, height, max_descent)

    def generate_table_image(self, valid_text, output_file):
        """
        Generate a table image showing ONLY the valid characters.
        Each character is placed at its correct hex position.
        Invalid characters leave empty cells.
        """
        if not valid_text:
            print("Error: No valid characters found")
            return

        # Create a 16x16 grid (0x00 to 0xFF)
        # Row index = high nibble (0-15), Col index = low nibble (0-15)
        grid = [[None for _ in range(16)] for _ in range(16)]
        
        # Get glyphs and place them in the correct position
        char_glyphs = {}
        max_width = 0
        max_height = 0
        
        for char in valid_text:
            code = ord(char)
            row = code >> 4      # High nibble (0-15)
            col = code & 0x0F    # Low nibble (0-15)
            
            glyph = self.glyph_for_character(char)
            char_glyphs[char] = glyph
            grid[row][col] = char
            
            max_width = max(max_width, glyph.width)
            max_height = max(max_height, glyph.height)

        # Calculate cell size based on font size
        padding_cell = max(8, self.font_size // 4)
        cell_size = max(self.font_size + padding_cell * 2, 32)
        
        if max_width + padding_cell > cell_size:
            cell_size = max_width + padding_cell
        if max_height + padding_cell > cell_size:
            cell_size = max_height + padding_cell

        # Image dimensions - 16 columns, 16 rows (0x00-0xFF)
        chars_per_row = 16
        total_rows = 16  # 0x00 to 0xFF
        
        # We'll only show rows that have at least one valid character
        # But we need to keep the hex positions correct
        first_row = 2  # Start from 0x20 (space) to skip control characters
        last_row = 15  # Up to 0xFF
        
        # Check which rows have valid characters
        rows_with_chars = []
        for row in range(first_row, last_row + 1):
            if any(grid[row][col] is not None for col in range(16)):
                rows_with_chars.append(row)
        
        if not rows_with_chars:
            print("Error: No valid characters found in display range")
            return

        # Image dimensions
        padding = max(10, self.font_size // 3)
        header_height = max(30, self.font_size + 8)
        row_label_width = max(40, self.font_size + 10)
        footer_height = max(35, self.font_size + 10)

        total_width = padding + row_label_width + (chars_per_row * cell_size) + padding
        total_height = padding + header_height + (len(rows_with_chars) * cell_size) + padding + footer_height

        # Create image
        img = Image.new('RGB', (total_width, total_height), color='lightyellow')
        draw = ImageDraw.Draw(img)

        # Font for labels
        try:
            label_font = ImageFont.truetype("C:/Windows/Fonts/arial.ttf", max(12, self.font_size // 2))
        except:
            try:
                label_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", max(12, self.font_size // 2))
            except:
                label_font = ImageFont.load_default()

        # Border
        draw.rectangle([0, 0, total_width-1, total_height-1], outline='black', width=2)

        # Grid lines
        draw.line([padding, padding + header_height, total_width - padding, padding + header_height], 
                  fill='lightgrey', width=1)
        draw.line([padding + row_label_width, padding, padding + row_label_width, total_height - padding - footer_height], 
                  fill='lightgrey', width=1)

        # "hex" label
        draw.text((padding + 5, padding + 5), "hex", fill='black', font=label_font)

        # Column headers (0-9, A-F)
        for col in range(chars_per_row):
            x = padding + row_label_width + col * cell_size + cell_size // 2
            y = padding + 5
            label = str(col) if col < 10 else chr(ord('A') + col - 10)
            bbox = draw.textbbox((0, 0), label, font=label_font)
            text_width = bbox[2] - bbox[0]
            draw.text((x - text_width//2, y), label, fill='black', font=label_font)

        # Row headers (2x, 3x, 4x, ..., Fx)
        for row_idx, row_num in enumerate(rows_with_chars):
            y = padding + header_height + row_idx * cell_size + cell_size // 2
            label = f"{row_num:x}x"
            bbox = draw.textbbox((0, 0), label, font=label_font)
            text_width = bbox[2] - bbox[0]
            text_height = bbox[3] - bbox[1]
            draw.text((padding + 5, y - text_height//2), label, fill='black', font=label_font)

        # Draw each character in its correct hex position
        for row_idx, row_num in enumerate(rows_with_chars):
            for col in range(chars_per_row):
                char = grid[row_num][col]
                if char is None:
                    continue  # Empty cell for invalid character
                    
                x = padding + row_label_width + col * cell_size + cell_size // 2
                y = padding + header_height + row_idx * cell_size + cell_size // 2

                glyph = char_glyphs.get(char)
                if glyph and glyph.width > 0 and glyph.height > 0:
                    glyph_img = Image.new('L', (glyph.width, glyph.height), color=255)
                    glyph_pixels = glyph_img.load()
                    
                    for i in range(glyph.height):
                        for j in range(glyph.width):
                            if glyph.bitmap.pixels[i * glyph.width + j]:
                                glyph_pixels[j, i] = 0

                    x_offset = x - glyph.width // 2
                    y_offset = y - glyph.height // 2
                    img.paste(glyph_img, (x_offset, y_offset))

        # Info text
        info_text = f"DEC = (row x 16) + column | Max Height: {max_height} Width: {max_width} | Total: {len(valid_text)} valid characters"
        try:
            bbox = draw.textbbox((0, 0), info_text, font=label_font)
            info_x = total_width - padding - bbox[2] - 10
            info_y = total_height - padding - 10
            draw.text((info_x, info_y), info_text, fill='black', font=label_font)
        except:
            info_x = total_width - padding - len(info_text) * 6 - 10
            info_y = total_height - padding - 10
            draw.text((info_x, info_y), info_text, fill='black', font=label_font)

        img.save(output_file)
        print(f"\nImage saved to: {output_file}")
        print(f"Size: {total_width}x{total_height} pixels")
        print(f"Valid characters: {len(valid_text)}")
        print(f"Max glyph: {max_width}x{max_height}")
        print(f"Cell size: {cell_size}x{cell_size}")
        print(f"Rows shown: {len(rows_with_chars)} (from {rows_with_chars[0]:x}x to {rows_with_chars[-1]:x}x)")

        return img

    def write_python(self, valid_text, font_file, output_py=None):
        """Write Python module with ONLY valid characters - using UTF-8"""
        if not valid_text:
            print("Error: No valid characters found")
            return

        _, height, baseline = self.text_dimensions(valid_text)

        bits = []
        widths = []
        offsets = []
        offset = 0

        for char in valid_text:
            glyph = self.glyph_for_character(char)

            if glyph.left >= 0:
                char_width = int(max(glyph.advance_width, glyph.width + glyph.left))
                left = glyph.left
            else:
                char_width = int(max(glyph.advance_width - glyph.left, glyph.width))
                left = 0

            offsets.append(offset)
            widths.append(char_width)
            outbuffer = Bitmap(char_width, height)

            y = height - glyph.ascent - baseline
            outbuffer.bitblt(glyph.bitmap, left, y)

            bit_string = outbuffer.bit_string()
            bits.append(bit_string)
            offset += len(bit_string)

        bit_string = ''.join(bits)

        text_escaped = valid_text.replace('\\', '\\\\').replace('"', '\\"').replace("'", "\\'")
        char_map = wrap_str(text_escaped)

        cmd_line = " ".join(map(shlex.quote, sys.argv))
        max_width = max(widths) if widths else 0

        if output_py is None:
            output = sys.stdout
        else:
            output = open(output_py, 'w', encoding='utf-8')
        
        print('# -*- coding: utf-8 -*-', file=output)
        print(f'# Converted from {font_file} using:', file=output)
        print(f'#     {cmd_line}', file=output)
        print(f'# Valid characters: {len(valid_text)}', file=output)
        print(file=output)

        print(f'MAP = {char_map}\n', file=output)
        print('BPP = 1', file=output)
        print(f'HEIGHT = {height}', file=output)
        print(f'MAX_WIDTH = {max_width}', file=output)
        print('_WIDTHS = \\', file=output)
        print(wrap_bytes(widths), file=output)
        print(file=output)

        byte_offsets = bytearray()
        bytes_table = [0xff, 0xffff, 0xffffff, 0xffffffff]
        bytes_required = bisect.bisect_left(bytes_table, offset, 0, 3) + 1
        for offset in offsets:
            byte_offsets.extend(offset.to_bytes(bytes_required, 'big'))

        print(f'OFFSET_WIDTH = {bytes_required}', file=output)
        print('_OFFSETS = \\', file=output)
        print(wrap_longs(byte_offsets), file=output)
        print(file=output)

        print('_BITMAPS =\\', file=output)
        byte_values = [int(bit_string[i:i+8], 2) for i in range(0, len(bit_string), 8)]
        print(wrap_bytes(byte_values), file=output)
        print("\nWIDTHS = memoryview(_WIDTHS)", file=output)
        print("OFFSETS = memoryview(_OFFSETS)", file=output)
        print("BITMAPS = memoryview(_BITMAPS)", file=output)
        
        if output_py is not None:
            output.close()
            print(f"Python module saved to: {output_py}")


def main():
    parser = argparse.ArgumentParser(
        prog='font2bitmap',
        description='''
            Convert characters from a truetype font to a python bitmap.
            Automatically filters invalid characters and generates both
            a Python module and a table image with ONLY valid characters.
        ''')

    parser.add_argument(
        'font_file',
        help='name of font file to convert.')

    parser.add_argument(
        'font_height',
        type=int,
        default=8,
        help='size of font to create bitmaps from.')

    parser.add_argument(
        '-width', '--font_width',
        type=int,
        default=None,
        help='width of font to create bitmaps from.')

    parser.add_argument(
        '-o', '--output_image',
        default='font_table.png',
        help='output PNG table image filename (default: font_table.png)')

    parser.add_argument(
        '-py', '--output_py',
        default=None,
        help='output Python module filename (default: fontname.py)')

    group = parser.add_argument_group(
        'character selection',
        'characters from the font to include in the bitmap.')

    excl = group.add_mutually_exclusive_group(required=True)
    excl.add_argument(
        '-c', '--characters',
        help='''integer or hex character values and/or ranges to include.
        For example: "65, 66, 67" or "32-127" or "0x30-0x39, 0x41-0x5a"''')

    excl.add_argument(
        '-s', '--string',
        help='''string of characters to include
        For example: "1234567890-."''')

    args = parser.parse_args()
    font_file = args.font_file
    height = args.font_height
    width = args.font_height if args.font_width is None else args.font_width
    
    all_chars = get_chars(args.characters) if args.string is None else args.string
    print(f"Requested characters: {len(all_chars)}")

    fnt = Font(font_file, width, height)
    
    # Filter to only valid characters
    valid_text = fnt.get_valid_characters(all_chars)
    print(f"Valid characters found: {len(valid_text)}")
    
    if not valid_text:
        print("Error: No valid characters found in font")
        sys.exit(1)

    # Generate table image
    fnt.generate_table_image(valid_text, args.output_image)

    # Generate Python module
    if args.output_py is None:
        base_name = os.path.splitext(os.path.basename(font_file))[0]
        args.output_py = f"{base_name}.py"
    
    fnt.write_python(valid_text, font_file, args.output_py)


if __name__ == '__main__':
    main()
