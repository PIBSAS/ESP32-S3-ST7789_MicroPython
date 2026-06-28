"""
hello.py

    Required font:
    - vga.py
    
    Writes "Hello!" in random colors at random locations on the display with 8px by 8 px font.
"""

import random
import time
import st7789
import tft_config
import vga as font

tft = tft_config.config(0)

def center(text):
    length = len(text)
    tft.text(
        font,
        text,
        tft.width() // 2 - length // 2 * font.WIDTH,
        tft.height() // 2 - font.HEIGHT,
        st7789.WHITE,
        st7789.RED)

def main():
    tft.init()

    tft.fill(st7789.RED)
    center("Hello!")
    time.sleep(2)
    tft.fill(st7789.BLACK)

    while True:
        for rotation in range(4):
            tft.rotation(rotation)
            tft.fill(st7789.BLACK)
            col_max = tft.width() - font.WIDTH*6
            row_max = tft.height() - font.HEIGHT

            for _ in range(128):
                tft.text(
                    font,
                    "Hello!",
                    random.randint(0, col_max),
                    random.randint(0, row_max),
                    st7789.color565(
                        random.getrandbits(8),
                        random.getrandbits(8),
                        random.getrandbits(8)),
                    st7789.color565(
                        random.getrandbits(8),
                        random.getrandbits(8),
                        random.getrandbits(8)))


main()
