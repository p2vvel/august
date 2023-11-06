from PIL import Image


def sepia(img: Image) -> Image:
    """
    Convert an image to sepia.

    Args:
        img (Image): The input image.

    Returns:
        Image: The sepia-converted image.
    """
    result = img.copy().convert("RGB")
    pixels = result.load()
    width, height = img.size
    for px in range(width):
        for py in range(height):
            r, g, b = pixels[px, py]
            new_r = int(r * 0.393 + g * 0.769 + b * 0.189)
            new_g = int(r * 0.349 + g * 0.686 + b * 0.168)
            new_b = int(r * 0.272 + g * 0.534 + b * 0.131)
            pixels[px, py] = (new_r, new_g, new_b)
    return result


def change_warmth(img: Image, ratio: int) -> Image:
    """
    Change the warmth of an image by a given ratio.

    Args:
        img (Image): The input image.
        ratio (int): The warmth ratio to apply.

    Returns:
        Image: The image with warmth adjusted by the specified ratio.
    """
    result = img.copy().convert("RGB")
    pixels = result.load()
    width, height = img.size
    for px in range(width):
        for py in range(height):
            r, g, b = pixels[px, py]
            pixels[px, py] = (r + ratio, g, b - ratio)
    return result
