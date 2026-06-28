"""
bitmap_fonts.py

    Required font:
    - fonts/bitmap/vga.py
    - fonts/bitmap/vga_8x16.py
    - fonts/bitmap/vga_bold_16.py
    - fonts/bitmap/vga_bold_16x32.py

    Cycles through all characters of four bitmap fonts on the display

"""

import time
import st7789
import tft_config
import vga as font1
import vga_8x16 as font2
import vga_bold_16 as font3
import vga_bold_16x32 as font4


tft = tft_config.config(0)


def main():
    tft.init()

    while True:
        for font in (font1, font2, font3, font4):
            tft.fill(st7789.BLUE)
            line = 0
            col = 0
            for char in range(font.FIRST, font.LAST):
                tft.text(font, chr(char), col, line, st7789.WHITE, st7789.BLUE)
                col += font.WIDTH
                if col > tft.width() - font.WIDTH:
                    col = 0
                    line += font.HEIGHT

                    if line > tft.height()-font.HEIGHT:
                        time.sleep(3)
                        tft.fill(st7789.BLUE)
                        line = 0
                        col = 0

            time.sleep(3)

main()
