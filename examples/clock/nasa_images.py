"""
nasa_images.py - Display a series of NASA images on the display from the
nasa_480x320/ folder.

Images courtesy of the NASA image and video gallery available at
https://images.nasa.gov/
"""

import random
import time, gc
import st7789
import tft_config
from machine import freq

tft = tft_config.config(1)

def main():

    """
    Decode and draw jpg on display
    """
    tft.init()

    while True:
        for image in range(1, 25):
            # If you dont upload clock folder to esp then delete clock/
            filename = f"clock/clock_{tft.width()}x{tft.height()}/nasa{image:02d}.jpg"
            tft.jpg(filename, 0, 0)  # Draw full screen jpg
            gc.collect()
            time.sleep(5)  # Wait 5 second

main()
# END CODE
