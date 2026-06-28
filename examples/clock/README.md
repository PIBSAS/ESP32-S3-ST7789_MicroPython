# clock.py

Displays a clock over a background image on the display.

The `tft_buttons.py` on the module can be used to set the time.

Background images courtesy of the NASA image and video gallery available at
https://images.nasa.gov/

The Font is Copyright 2018 The Pacifico Project Authors (https://github.com/googlefonts/Pacifico)
This Font Software is licensed under the SIL Open Font License, Version 1.1.
This license is copied below, and is also available with a FAQ at:
http://scripts.sil.org/OFL

## Required:

- font: [pacifico_40.py](../../fonts/truetype/pacifico_40.py)
- Folders:
  - Landscape: [clock_320x170](/examples/clock/)
- Optional but already in the firmware, [tft_buttons.py](/configs/esp32s3-N16R8/tft_buttons.py)
----

### PACIFICO 40 font:

![Image](/docs/pacifico_40.png)

----

# nasa_images.py

## Requireed:

- images: 
    - Landscape: [clock_320x170/nasaNN.jpg](/examples/clock_320x170/) all images in the folder
    - Portrait: [clock_170x320/nasaNN.jpg](/examples/clock_170x320/) all images in the folder

Display a series of NASA images on the display from the
`nasa_WIDTHxHEIGHT/` folder.

Images courtesy of the NASA image and video gallery available at
[https://images.nasa.gov/](https://images.nasa.gov/)
