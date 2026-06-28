##mono_fonts.py

## Required fonts:

- [inconsolata_16.py](../../fonts/truetype/inconsolata_16.py)
- [inconsolata_32.py](../../fonts/truetype/inconsolata_32.py)
- [inconsolata_64.py](../../fonts/truetype/inconsolata_64.py)

Test for `monofont2bitmap` converter and `bitmap` method. This is the older method of
converting monofonts to bitmaps. See the newer method in `chango_fonts/chango.py` that works with
mono and proportional fonts using the `write` method.

TrueType fonts use `write` method.
