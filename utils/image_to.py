#--------------------------------------------#
# 2026 by Luciano's tech
# https://sites.google.com/view/lucianostech
#--------------------------------------------#
"""
Require:
libcairo-2.dll

You can install with winget:
winget install tschoonj.GTKForWindows

After install, close all terminals and start again the python virtual environment
Now will find the .dll needed by cairosvg package
"""
import sys, subprocess, io

def is_dependencies_installed():
    """
    Verifica si las dependencias están instaladas.
    Si alguna falta, la instala automáticamente.

    :return: None
    """
    packages = ["Pillow", "cairosvg"]
    for package in packages:
        try:
            subprocess.check_output([sys.executable, "-m", "pip", "show", package])
        except subprocess.CalledProcessError:
            subprocess.check_call([sys.executable, "-m", "pip", "install", package])

is_dependencies_installed()

from pathlib import Path
from PIL import Image
import cairosvg

#------- CONFIG -------#

OUTPUT_FORMAT = "PNG" # PNG or JPEG
QUALITY = 95          # Just for JPEG so dont need touch

LOGOS = (
    (64, 64),
    (128, 128),
    (240, 240),
    (80, 160),
    (160, 80),
    (128, 160),
    (160, 128),
    (135, 240),
    (240, 135),
    (170, 320),
    (320, 170),
    (172, 320),
    (320, 172),
    (240, 320),
    (320, 240),
    (320, 480),
    (480, 320)
)
#----------------------#

# Prioridad, Priority: SVG > PNG > JPG > JPEG
PRIORITY = {
    ".svg": 0,
    ".png": 1,
    ".jpg": 2,
    ".jpeg": 3,
}

folder_base = Path(__file__).resolve().parent.name

def save_image(img, folder_base, stem, width, height):
    """
    Save the image on selected OUTPUT_FORMAT in a folder
    Guarda la imagen en el formato seleccionado en OUTPUT_FORMAT en una carpe
    """
    folder_name = f"{folder_base}_{width}x{height}"
    output_dir = Path(folder_name)
    output_dir.mkdir(parents=True, exist_ok=True)

    if OUTPUT_FORMAT.upper() == "PNG":
        output_path = output_dir / f"{stem}-{width}x{height}.png"
        img.save(output_path, "PNG", optimize=True)
    elif OUTPUT_FORMAT.upper() == "JPEG":
        output_path = output_dir / f"{stem}-{width}x{height}.jpg"
        img.convert("RGB").save(output_path, "JPEG", quality=QUALITY)
    elif OUTPUT_FORMAT.upper() == "JPG":
        output_path = output_dir / f"{stem}-{width}x{height}.jpg"
        img.convert("RGB").save(output_path, "JPEG", quality=QUALITY)
    else:
        raise ValueError(f"Unsopported format, Formato no soportado: {OUTPUT_FORMAT}")

    return output_path

# Agrupar por nombre base, Group by basename
sources = {}

for file in Path(".").iterdir():

    if not file.is_file():
        continue

    ext = file.suffix.lower()

    if ext not in PRIORITY:
        continue

    stem = file.stem

    if stem not in sources:
        sources[stem] = file
    else:
        current = sources[stem]

        if PRIORITY[ext] < PRIORITY[current.suffix.lower()]:
            sources[stem] = file

for source in sources.values():

    print(f"Procesando, processing: {source}")

    ext = source.suffix.lower()
    stem = source.stem
    #SVG
    if ext == ".svg":

        for width, height in LOGOS:

            png_data = cairosvg.svg2png(
                url=str(source),
                output_width=width,
                output_height=height
            )

            img = Image.open(io.BytesIO(png_data))
            output = save_image(img, folder_base, stem, width, height)

            print(f"OK -> {output}")
    # PNG/JPG/JPEG
    else:

        img = Image.open(source)

        for width, height in LOGOS:

            resized = img.resize(
                (width, height),
                Image.Resampling.LANCZOS
            )

            output = save_image(resized, folder_base, stem, width, height)

            print(f"OK -> {output}")

print("Proceso terminado.Finished process.")
