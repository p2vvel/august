from PIL import Image, ImageOps

from . import schemas


def sepia(img: Image) -> Image:
    """Convert image to sepia"""
    result = img.copy().convert("RGB")
    pixels = result.load()
    width, height = img.size
    for px in range(width):
        for py in range(height):
            r, g, b = pixels[px, py]
            newR = int(r * 0.393 + g * 0.769 + b * 0.189)
            newG = int(r * 0.349 + g * 0.686 + b * 0.168)
            newB = int(r * 0.272 + g * 0.534 + b * 0.131)
            pixels[px, py] = (newR, newG, newB)
    return result


def change_warmth(img: Image, ratio: int) -> Image:
    """Change image warmth by given ratio"""
    result = img.copy().convert("RGB")
    pixels = result.load()
    width, height = img.size
    for px in range(width):
        for py in range(height):
            r, g, b = pixels[px, py]
            pixels[px, py] = (r + ratio, g, b - ratio)
    return result


def change_colors(img: Image, color: schemas.Color) -> Image:
    """Change image colors according to color value"""
    match color:
        case schemas.Color.NONE:
            return img
        case schemas.Color.BLACK_AND_WHITE:
            return ImageOps.grayscale(img.convert("RGB"))
        case schemas.Color.SEPIA:
            return sepia(img)
        case schemas.Color.NEGATIVE:
            return ImageOps.invert(img.convert("RGB"))
        case schemas.Color.WARM:
            return change_warmth(img, 15)
        case schemas.Color.COLD:
            return change_warmth(img, -15)
        case _:
            raise ValueError("Invalid color value")
