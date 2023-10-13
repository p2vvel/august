from PIL import Image as PILImage, ImageOps, ImageFilter, ImageChops
from . import utils


class AugustImage:
    def __init__(self, img_path: str) -> None:
        self.img = PILImage.open(img_path)

    def save(self, filename: str) -> None:
        self.img.save(filename)

    def show(self) -> None:
        self.img.show()

    def mirror(self) -> None:
        self.img = self.img.transpose(PILImage.FLIP_LEFT_RIGHT)

    def flip(self) -> None:
        self.img = self.img.transpose(PILImage.FLIP_TOP_BOTTOM)

    def _sepia(self) -> None:
        self.img = utils.sepia(self.img)

    def _black_and_white(self) -> None:
        self.img = ImageOps.grayscale(self.img.convert("RGB"))

    def _color_temperature(self, ratio: int) -> None:
        self.img = utils.change_warmth(self.img, ratio)

    def rotate(self, angle: float, expand: bool = False) -> None:
        self.img = self.img.rotate(angle=angle, expand=expand)

    def noise(self) -> None:
        pass

    def blur(self, pixel_radius: int) -> None:
        self.img = self.img.filter(ImageFilter.BoxBlur(pixel_radius))

    def crop(self, x_min: int, y_min: int, x_max: int, y_max: int) -> None:
        self.img = self.img.crop((x_min, y_min, x_max, y_max))

    def offset(self, x_offset: int, y_offset: int) -> None:
        self.img = ImageChops.offset(self.img, x_offset, y_offset)

    # noise


if __name__ == "__main__":
    pass
    from pathlib import Path
    test_path = Path("/home/pawel/august/august/images/tests/resources/")
    test_img = test_path / "test_image.jpg"
    img = AugustImage(test_img)
    img.mirror()
    # img.flip()
    # img._sepia()
    # img._black_and_white()
    # img._color_temperature(-50)
    # img.rotate(30)
    # img.crop(100, 0, 800, 400)
    # img.offset(0, 100)
    # img.zoom(100, 100, 4)
    img.show()
    img.save("test_image_mirrored.jpg")

    base_filename = "test_image"
    extra_names = ("mirror", "flip", "sepia", "bw", "warm", "rotated", "cropped", "offset", "zoom")