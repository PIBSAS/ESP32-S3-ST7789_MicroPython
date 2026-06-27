#--------------------------------------------#
# 2026 by Luciano's tech
# https://sites.google.com/view/lucianostech
#--------------------------------------------#
import sys, subprocess
def is_dependencies_installed():
    """
    Verifica si las dependencias están instaladas.
    Si alguna falta, la instala automáticamente.

    :return: None
    """
    packages = ["Pillow"]
    for package in packages:
        try:
            subprocess.check_output([sys.executable, "-m", "pip", "show", package])
        except subprocess.CalledProcessError:
            subprocess.check_call([sys.executable, "-m", "pip", "install", package])

is_dependencies_installed()

from pathlib import Path
from PIL import Image


"""
The folder saving resized images have the name clock_320x172
Which is made by PATH+WIDTH+HEIGHT

The image have a name nasaNN.jpg where NN are numbers from 01 to MAX
Which is made by NAME+01 to MAX.jpg

QUALITY is the JPEG QUALITY

PUT SOURCE IMAGES IN THE SAME PATH OF THIS SCRIPT
"""

"""
La carpeta que guarda las imagenes redimensionadas tiene el nombre clock_320x172
Es decir, PATH+WIDTH+HEIGHT

Cada imagen tiene el nombre nasaNN.jpg donde NN son numeros desde 01 a MAX
Es decir, NAME+01 hasta MAX,jpg

QUALITY es la alidad JPEG

PONE LAS IMAGENES A CONVERTIR EN LA MISMA UBICACION QUE ESTE SCRIPT
"""
#=======CONFIG=======#

PATH = "clock" 
WIDTH = 320
HEIGHT = 172
MAX = 25
NAME = "nasa"
QUALITY = 95

#===================#

# Carpeta de salida
output_dir = Path(f"{PATH}_{WIDTH}x{HEIGHT}")
output_dir.mkdir(exist_ok=True)

for i in range(1, (MAX + 1)):
    filename = f"{NAME}{i:02d}.jpg"

    try:
        img = Image.open(filename)

        resized = img.resize(
            (WIDTH, HEIGHT),
            Image.Resampling.LANCZOS
        )

        output_file = output_dir / filename

        resized.save(
            output_file,
            "JPEG",
            quality=QUALITY
        )

        print(f"OK -> {output_file}")

    except Exception as e:
        print(f"Error en {filename}: {e}")

print("Proceso terminado.")
