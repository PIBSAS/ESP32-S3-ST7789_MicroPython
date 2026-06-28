# Example Programs

All of the example programs requrire a `tft_config.py` module to confiure the display. Some examples
also require a `tft_buttons.py` module to configure buttons.  See the config directory for example
configuration modules for various devices and displays.

***Special Note for ESP32 devices:***

To use SPI baudrates above 26.6MHz you must use my firmware or modify the micropython
source code to increase the SPI baudrate limit by adding `SPI_DEVICE_NO_DUMMY` to the
`.flag member` of the `spi_device_interface_config_t struct` in the `machine_hw_spi_init_internal.c`
file.  Not doing so will cause the ESP32 to crash if you use a baudrate that is too high.


## bitarray.py

- An example using `map_bitarray_to_rgb565` to draw sprites


## bitmap_fonts/bitmap_fonts.py

- Required fonts:
    - [fonts/bitmap/vga.py](../fonts/bitmap/vga.py)
    - [fonts/bitmap/vga16.py](../fonts/bitmap/vga16.py)
    - [fonts/bitmap/vgabold16.py](../fonts/bitmap/vgabold16.py)
    - [fonts/bitmap/vgabold32.py](../fonts/bitmap/vgabold32.py)

Cycles through all characters of four bitmap fonts on the display.


## chango_fonts/chango.py

- Required fonts:
    - [chango_16.py](../fonts/bitmap/chango_16.py)
    - [chango_32.py](../fonts/bitmap/chango_16.py)
    - [chango_64.py](../fonts/bitmap/chango_16.py)

Proportional font test for font2bitmap converter.


## clock/clock.py
    Requireed:
    - font: pacifico40.py
    - tft_buttons.py
    - images: 
        - Landscape: clock/clock_320x170/nasaNN.jpg all images in the folder
        - Portrait: clock/clock_170x320/nasaNN.jpg all images in the folder
    
    Displays a clock over a background image on the display.

    The buttons on the module can be used to set the time.

    Background images courtesy of the NASA image and video gallery available at
    https://images.nasa.gov/

    The Font is Copyright 2018 The Pacifico Project Authors (https://github.com/googlefonts/Pacifico)
    This Font Software is licensed under the SIL Open Font License, Version 1.1.
    This license is copied below, and is also available with a FAQ at:
    http://scripts.sil.org/OFL


## clock/nasa_images.py
    Requireed:
    - images: 
        - Landscape: clock/clock_320x170/nasaNN.jpg all images in the folder
        - Portrait: clock/clock_170x320/nasaNN.jpg all images in the folder
    
    Display a series of NASA images on the display from the
    nasa_WIDTHxHEIGHT/ folder.

    Images courtesy of the NASA image and video gallery available at
    https://images.nasa.gov/


## feathers.py

    Smoothly scroll rainbow-colored mirrored random curves across the display.


## hello.py

    Required font: vga2_bold_16x32.py
    Writes "Hello!" in random colors at random locations on the display.


## tiny_hello.py

    Required font: vga1_8x8.py
    Writes "Hello!" in random colors at random locations on the display.


## hola.py

    Required font: vga2_bold_16x32.py
    Writes "Hola!" in random colors at random locations on the display.

    
## hershey.py

    Required font already included on firware: greeks, italicc, italiccs, meteo, romanc, romancs, romand, romanp, romans, scriptc, scripts
    Demo program that draws greetings on display cycling thru hershey fonts and colors.


## jpg/jpg.py

    Required:
    - images:
        - Landscape: jpg/bigbuckbunny-320x170.jpg
        - Portrait: jpg/bigbuckbunny-170x320.jpg
    
    Draw a full screen jpg using the slower but less memory intensive method of blitting
    each Minimum Coded Unit (MCU) block. Usually 8×8pixels but can be other multiples of 8.

    bigbuckbunny.jpg (c) copyright 2008, Blender Foundation / www.bigbuckbunny.org


## jpg/alien.py

    Required:
        - image: alien.jpg
    
    Randomly draw alien.jpg with alpha-channel masking

    The alien.png is from the Erik Flowers Weather Icons available from
    https://github.com/erikflowers/weather-icons and is licensed under
    SIL OFL 1.1


## png/png.py

    Required:
    - images:
        - Landscape: png/bigbuckbunny-320x170.png
        - Portrait: png/bigbuckbunny-170x320.png

    Draw a full screen png.

    bigbuckbunny.png (c) copyright 2008, Blender Foundation / www.bigbuckbunny.org


## png/png_bounce.py

    Required:
    - image: alien.png
    
    Bounce a png around the display to test png decoder and visibility clipping.


## png/alien.py

    Required:
    - image: alien.png
    
    Randomly draw alien.png with alpha-channel masking

    The alien.png is from the Erik Flowers Weather Icons available from
    https://github.com/erikflowers/weather-icons and is licensed under
    SIL OFL 1.1


## png/logo.py

    Required:
    - images: 
        - Landscape: png/logo-widthxheight.png all images in the folder

    Draw different sized png MicroPython logos to test the png decoder and clipping. 
    Copy the png logo files to the same directory as this file.

    The MicroPython logo is copyright George Robotics Ltd.


## mono/mono_fonts.py

### Required fonts:

- [inconsolata_16.py](../fonts/bitmap/inconsolata_16.py)
- [inconsolata_32.py](../fonts/bitmap/inconsolata_32.py)
- [inconsolata_64.py](../fonts/bitmap/inconsolata_64.py)

Test for `monofont2bitmap` converter and `bitmap` method. This is the older method of
converting monofonts to bitmaps. See the newer method in `chango_fonts/chango.py` that works with
mono and proportional fonts using the `write` method.


## noto/noto_fonts.py

### Required fonts: 

- [NotoSans.py](../fonts/truetype/NotoSans.py)
- [NotoSerif.py](../fonts/truetype/NotoSerif.py)
- [NotoSansMono.py](../fonts/truetype/NotoSansMono.py)

Writes the names of three Noto fonts centered on the display
using the font. The fonts were converted from True Type fonts using
the [font2bitmap](../utils/font2bitmap.py) utility.


## pinball.py

    Required: fonts= vga1_8x8.py, vga1_bold_16x32.py and tft_buttons.py
    
    Minimal pinball game in MicroPython based on code from Ten Minute Physics Tutorial
    "How to write a pinball simulation"

    Tutorial Links:
        https://matthias-research.github.io/pages/tenMinutePhysics/
        https://youtu.be/NhVUCsXp-Uo

    GamePlay Video:
        https://youtu.be/y0B3i_UmEU8


## roids.py

    Required: tft_buttons.py
    
    Asteroids style game demo using polygons.


## scroll.py

    Required font: vga1_bold_16x16.py
    
    Smoothly scroll all characters of a font up the display.
    Fonts heights must be even multiples of the screen height (i.e. 8 or 16 pixels high).


## tiny_toasters.py

    Required: tiny_toasters/ttoast_bitmaps.py
    
    Flying Tiny Toasters for smaller displays (like the ST7735) Adapted to 1.9" st7789

    Uses spritesheet from CircuitPython_Flying_Toasters pendant project
    https://learn.adafruit.com/circuitpython-sprite-animation-pendant-mario-clouds-flying-toasters

    Convert spritesheet bmp to tft.bitmap() method compatible python module using:
        python3 ./sprites2bitmap.py ttoasters.bmp 32 32 4 > ttoast_bitmaps.py


## toasters.py

    Required: toasters/toast_bitmaps.py
    
    Flying Toasters

    Uses spritesheet from CircuitPython_Flying_Toasters pendant project
    https://learn.adafruit.com/circuitpython-sprite-animation-pendant-mario-clouds-flying-toasters

    Convert spritesheet bmp to tft.bitmap() method compatible python module using:
        python3 ./sprites2bitmap.py toasters.bmp 64 64 4 > toast_bitmaps.py


## toasters_jpg.py

    Required: toasters_jpg/toaster.jpg
    
    An example using a jpg sprite map to draw sprites on T-Display.  This is an older version of the
    toasters.py and tiny_toasters example.  It uses the jpg_decode() method to grab a bitmap of each
    sprite from the toaster.jpg sprite sheet.

    Youtube video: https://youtu.be/0uWsjKQmCpU

    spritesheet from CircuitPython_Flying_Toasters
    https://learn.adafruit.com/circuitpython-sprite-animation-pendant-mario-clouds-flying-toasters


## watch.py

    Required:
    - images:
        - Landscape: watch/face_320x170.jpg
        - Portrait: watch/face_170x320.jpg
    
    Analog Watch Display using jpg for the face and filled polygons for the hands
    Requires face_{width}x{height}.jpg in the same directory as this script. See the create_face.py
    script for creating a face image for a given sized display.

    Previous version video: https://youtu.be/NItKb6umMc4


# Utility Programs

## utils/cfg_helper.py

    Required font: vga1_8x8.PY
    
    Utility to help with determining colstarts, rowstarts, color_order and inversion settings for
    for a display.

    Set the `HEIGHT` and `WIDTH` constants to the physical size of your display or use the {Cc} keys
    to set the number of columns and the {Rr} keys to set the number of rows for your display.

    The program starts by filling the display with RED and draws a WHITE rectangle around the
    perimeter.

    - If the display background is RED, the color configuration is correct.
    - If the display background is BLUE, toggle the color_order from RGB to BGR using the {Oo} keys.
    - If the display background is YELLOW, toggle the inversion from False to True using the {Ii}
    keys.
    - If the display background is CYAN, toggle both the color_order from RGB to BGR using the {Oo}
    keys and toggle the inversion from False to True using the {Ii} keys.

    Once you have a display with a RED background you can step through RED, GREEN and BLUE
    backgrounds using the {Bb} keys.

    Use the {Yy}, {Xx}, {Vv}, {Ll} and {Hh} keys to toggle the MADCTL_MY, MADCTL_MX, MADCTL_MV,
    MADCTL_ML and MADCTL_ML bits of the MADCTL register.

    The MADCTL_MY bit sets the Page Address Order.
    The MADCTL_MX bit sets the Column Address Order
    The MADCTL_MV bit sets the Page/Column Order
    The MADCTL_ML bit sets the Line Address Order
    The MADCTL_MH bit sets the Display Data Latch Order

    Observe the edges of the display, there should be a 1 pixel wide rectangle outlining the
    display. If one of the lines are not showing or you see random pixels on the outside of the
    white rectangle your display requires a colstart and/or rowstart offset. Some displays have a
    frame buffer memory larger than the physical LCD or LED matrix. In these cases the driver must
    be configured with the position of the first physical column and row pixels relative to the
    frame buffer.  Each rotation setting of the display may require different colstart and rowstart
    values.

    Use the 'W' and 'S' keys to increase or decrease the rowstart values by 10.
    Use the 'w' and 's' keys to increase or decrease the rowstart values by 1.

    Use the 'A' and 'D' keys to increase or decrease the colstart values by 10.
    Use the 'a' and 'd' keys to increase or decrease the colstart values by 1.

    Use the '+' and '-' keys to change the displays rotation.
    Use the '0' key to reset the rotation, the colstart and rowstart values to 0.

    Once you have determined the colstart and rowstart values for the rotations you are going to
    use, press the {Pp} key to print the current configuration values. You can use these values to
    support a display that does not work with the default values.

## utils/codeformat.py

## utils/create_face_jpg.py

    Required font: utils/LibreBaskerville-Regular.ttf
    
    Create a watch face_{width}x{height}.jpg file for a given width and height.


## utils/font2bitmap.py

    Font handling classes are from Dan Bader blog post on using freetype http://dbader.org/blog/monochrome-font-rendering-with-freetype-and-python


## utils/font_from_romfont.py

    Convert fonts from the font-bin directory of spacerace's https://github.com/spacerace/romfont repo.

    Reads all romfont bin files from the specified -input-directory (-i) and writes
    python font files to the specified -output-directory (-o).  Optionally limiting
    characters included to -first-char (-f) thru -last-char (-l).
    
    Example:
    
        font_from_romfont -i font-bin -o pyfont -f 32 -l 127
    
    requires argparse


## utils/hershey_to_poly.py

    Required: utils/arial.ttf


## utils/hershey_to_py.py

    Convert Hershey font data to python module.
    
    Usage: hershey_to_py.py <glyph_file> [map_file]
    
    The glyph_file (hf) is the Hershey font data file. The map_file (hmp) is an optional file that maps
    the Hershey font data to a character set.  The hershey_to_py.py script is compatible with the output
    from my fork of LingDong's ttf2hershey python2 program available from my github repository at
    https://github.com/russhughes/ttf2hershey.  Not all TrueType fonts can be converted. Some may
    result in a font with out-of-order or missing characters.
    
    A Hershey font file is a text file with the following format:
    
    Optional header lines:
    
    # WIDTH = 40        width of the font
    # HEIGHT = 45       height of the font
    # FIRST = 32        first character in the font
    # LAST = 127        last character in the font
    
    Comment lines start with a # and are ignored with the exception of the optional header lines.
    
    Glyph data lines have the following format:
    
    Bytes 1-5:  The character number
    Bytes 6-8:  The number of vector pairs in the glyph
    Bytes   9:  left hand position
    Bytes  10:  right hand position
    Bytes  11+: The vector data as a string of characters, 2 characters per vector.
    
    Vector values are relative to the ascii value of 'R'. A value of " R" non-drawing move to operation.
    
    Example:
    
       45  6JZLBXBXFLFLB
    
        Character number: 45 (ASCII '-')
        Number of vectors: 6
        Left hand position: J (ascii value 74 - 82 = -8)
        Right hand position: Z (ascii value 90 - 82 = 8)
        Vector data: LBXBXFLFLB
    
        The vector data is interpreted as follows:
    
            LB - Line to (-6, -16)
            XB - Line to (6, -16)
            XF - Line to (6, -12)
            LF - Line to (-6, -12)
            LB - Line to (-6, -16)
    
    
    A Hershey Map file is a text file with the following format:
    
    Comment lines start with a # and are ignored.
    
    Map data lines have the following format:
    
    Number of the first glyph to include in the font followed by space and the number of the last glyph
    in the font.  If the last glyph is 0 then only the first glyph is included.
    
    Example:
    
    32 64
    65 127

## utils/howto-convert-to-jpg

    You can convert images to compatible jpg's by using ImageMagick's convert
    utility by specifying the output type as TrueColor. ImageMagick downloads
    are available from https://imagemagick.org/ for Linux, OSX, Windows and
    other operating systems.
    
    The wi-alien.svg icon is from https://github.com/erikflowers/weather-icons licensed under SIL OFL 1.1
        
    - convert wi-alien.svg -type TrueColor alien.jpg


## utils/image_to.py

    Require:
    - libcairo-2.dll
    
    You can install with winget:
    - winget install tschoonj.GTKForWindows
    
    After install, close all terminals and start again the python virtual environment
    Now will find the .dll needed by cairosvg package

    Convert images to PNG or JPG from SVG > PNG > JPG > JPEG for differents resolutions:
    64x64, 128x128, 240x240, 80x160, 160x80, 128x160, 160x128, 135x240, 240x135, 170x320, 320x170, 172x320, 320x172, 240x320, 320x240, 320x480, 480x320

    Saving to a folder with resolution name and the images added the resolution to the name.


## utils/image_to_v2.py
    Require:
    - libcairo-2.dll
    
    You can install with winget:
    - winget install tschoonj.GTKForWindows
    
    After install, close all terminals and start again the python virtual environment
    Now will find the .dll needed by cairosvg package

    Convert images to PNG or JPG from SVG > PNG > JPG > JPEG for differents resolutions:
    64x64, 128x128, 240x240, 80x160, 160x80, 128x160, 160x128, 135x240, 240x135, 170x320, 320x170, 172x320, 320x172, 240x320, 320x240, 320x480, 480x320
    
    Saving to a folder with resolution name, with image with his namme.


## utils/imgtobitmap.py

    Convert image file to python module for use with blit_bitmap.

    Usage imgtobitmap image_file bits_per_pixel >image.py


## utils/jpg_converter.py

    The folder saving resized images have the name clock_320x172
    Which is made by PATH+WIDTH+HEIGHT
    
    The image have a name nasaNN.jpg where NN are numbers from 01 to MAX
    Which is made by NAME+01 to MAX.jpg
    
    QUALITY is the JPEG QUALITY
    
    PUT SOURCE IMAGES IN THE SAME PATH OF THIS SCRIPT


## utils/maketoast

    grab sprites from spritesheet using ImageMagick and convert to bitmap format.

## utils/monofont2bitmap.py

    Convert characters from monospace truetype fonts to a python bitmap
        for use with the bitmap method in the st7789 and ili9342 drivers.
    
    positional arguments:
    
      font_file             Name of font file to convert.
      font_size             Size of font to create bitmaps from.
      bits_per_pixel        The number of bits (1..8) to use per pixel.
    
    optional arguments:
    
      -h, --help            show this help message and exit
      -f FOREGROUND, --foreground FOREGROUND
                            Foreground color of characters.
      -b BACKGROUND, --background BACKGROUND
                            Background color of characters.
    
    character selection:
      Characters from the font to include in the bitmap.
    
      -c CHARACTERS, --characters CHARACTERS
                            integer or hex character values and/or ranges to
                            include.
    
                            For example: "65, 66, 67" or "32-127" or
                            "0x30-0x39, 0x41-0x5a"
    
      -s STRING, --string STRING
                            String of characters to include For example:
                            "1234567890-."


## utils/png_from_font.py

    Imports all the python font files from the specified -input-directory (-i) and
    creates png samples of each font in the specified -output-directory (-o).
    
    Example:
        png_from_font.py font_directory png_directory
    
    Requires argparse, importlib and pypng

## utils/sprites2bitmap.py

    Convert a sprite sheet image to python a module for use with indexed bitmap method.
    Sprite sheet width and height should be a multiple of sprite width and height. There
    should be no extra pixels between sprites. All sprites will share the same palette.

    Usage:
        sprites2bitmap image_file spite_width sprite_height bits_per_pixel  >sprites.py

    MicroPython:
        import sprites
        ... tft config and init code ...
        tft.bitmap(sprites, x, y, index)
