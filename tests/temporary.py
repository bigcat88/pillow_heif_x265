import pillow_heif
from PIL import Image

from pillow_heif_x265 import get_path

if __name__ == "__main__":
    print(pillow_heif.libheif_info()["encoders"])
    print("pillow_heif_x265: ", get_path())
    pillow_heif.load_libheif_plugin(get_path())
    print(pillow_heif.libheif_info()["encoders"])

    pillow_heif.register_heif_opener()
    im = Image.effect_mandelbrot((256, 256), (-3, -2.5, 2, 2.5), 100)
    im.save("test.heic")
