from PIL import Image as PILImage
from PIL import ImageChops, ImageFilter, ImageOps

from . import utils


class AugustImageMixin:
    def _mirror(self) -> None:
        self.img = self.img.transpose(PILImage.FLIP_LEFT_RIGHT)

    def _flip(self) -> None:
        self.img = self.img.transpose(PILImage.FLIP_TOP_BOTTOM)

    def _sepia(self) -> None:
        self.img = utils.sepia(self.img)

    def _black_and_white(self) -> None:
        self.img = ImageOps.grayscale(self.img.convert("RGB"))

    def _color_temperature(self, ratio: int) -> None:
        self.img = utils.change_warmth(self.img, ratio)

    def _rotate(self, angle: float, expand: bool = False) -> None:
        self.img = self.img.rotate(angle=angle, expand=expand)

    def _noise(self) -> None:
        pass

    def _blur(self, pixel_radius: int) -> None:
        self.img = self.img.filter(ImageFilter.BoxBlur(pixel_radius))

    def _crop(self, x_min: int, y_min: int, x_max: int, y_max: int) -> None:
        self.img = self.img.crop((x_min, y_min, x_max, y_max))

    def _offset(self, x_offset: int, y_offset: int) -> None:
        self.img = ImageChops.offset(self.img, x_offset, y_offset)
