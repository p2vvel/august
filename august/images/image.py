import random

from PIL import Image as PILImage, ImageOps, ImageFilter, ImageChops
from . import utils


class AugustImage:
    def __init__(self, img_path: str) -> None:
        self.img = PILImage.open(img_path)

    def save(self, filename: str) -> None:
        self.img.save(filename)

    def show(self) -> None:
        self.img.show()

    def mirror(self, p: float = 0.5) -> None:
        if random.random() <= p:
            self._mirror()

    def flip(self, p: float = 0.5) -> None:
        if random.random() <= p:
            self._flip()

    def color_change(self, p: float = 0.5) -> None:
        if random.random() <= p:
            if random.random() <= p:
                self._sepia()
            else:
                self._black_and_white()

    def color_temperature(self, p: float = 0.5, ratio_min: int = -50, ratio_max: int = 50) -> None:
        if random.random() <= p:
            ratio = random.randint(ratio_min, ratio_max)
            self._color_temperature(ratio)

    def rotate(self, p: float = 0.5, angle_min: int = -45, angle_max: int = 45) -> None:
        if random.random() <= p:
            angle = random.randint(angle_min, angle_max)
            self._rotate(angle)

    def blur(self, p: float = 0.5, pixel_radius_min: int = 1, pixel_radius_max: int = 5) -> None:
        if random.random() <= p:
            pixel_radius = random.randint(pixel_radius_min, pixel_radius_max)
            self._blur(pixel_radius)

    def offset(self, p: float = 0.5, x_offset_min: int = -10, x_offset_max: int = 10, y_offset_min: int = -10,
               y_offset_max: int = 10) -> None:
        if random.random() <= p:
            x_offset = random.randint(x_offset_min, x_offset_max)
            y_offset = random.randint(y_offset_min, y_offset_max)
            self._offset(x_offset, y_offset)

    def crop(self, p: float = 0.5, min_width: float = 0.2, max_width: float = 0.9, min_height: float=0.2, max_height=0.9) -> None:
        if random.random() <= p:
            width, height = self.img.size
            crop_width = random.randint(int(min_width * width), int(max_width * width))
            crop_height = random.randint(int(min_height * height), int(max_height * height))
            x_min = random.randint(0, width - crop_width)
            y_min = random.randint(0, height - crop_height)
            x_max = x_min + crop_width
            y_max = y_min + crop_height
            self._crop(x_min, y_min, x_max, y_max)

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
