import random

from PIL import Image as PILImage

from august.images.config import AugustImageConfig
from august.images.decorators import AugustImageMark, mark_augmentation
from august.images.mixins import AugustImageMixin
from august.mixins import ExecuteAugmentationMixin


class AugustImage(AugustImageMixin, ExecuteAugmentationMixin):
    _augmentations = AugustImageMark.augmentations

    def __init__(self, img_path: str, config: AugustImageConfig = AugustImageConfig()) -> None:
        self.img = PILImage.open(img_path)
        self.config = config

    def save(self, filename: str) -> None:
        self.img.save(filename)

    def show(self, title: str | None = None) -> None:
        self.img.show(title=title)

    @mark_augmentation
    def mirror(self, p: float = 0.5) -> None:
        if random.random() <= p:
            self._mirror()

    @mark_augmentation
    def flip(self, p: float = 0.5) -> None:
        if random.random() <= p:
            self._flip()

    @mark_augmentation
    def color_change(self, p: float = 0.5) -> None:
        if random.random() <= p:
            color_foo = random.choice((self._sepia, self._black_and_white))
            color_foo()

    @mark_augmentation
    def color_temperature(self, p: float = 0.5, ratio_min: int = -50, ratio_max: int = 50) -> None:
        if random.random() <= p:
            ratio = random.randint(ratio_min, ratio_max)
            self._color_temperature(ratio)

    @mark_augmentation
    def rotate(self, p: float = 0.5, angle_min: int = -89, angle_max: int = 89) -> None:
        if random.random() <= p:
            angle = random.randint(angle_min, angle_max)
            self._rotate(angle)

    @mark_augmentation
    def blur(self, p: float = 0.5, pixel_radius_min: int = 1, pixel_radius_max: int = 5) -> None:
        if random.random() <= p:
            pixel_radius = random.randint(pixel_radius_min, pixel_radius_max)
            self._blur(pixel_radius)

    @mark_augmentation
    def offset(
        self,
        p: float = 0.5,
        x_offset_min: float = -0.5,
        x_offset_max: float = 0.5,
        y_offset_min: float = -0.5,
        y_offset_max: float = 0.5,
    ) -> None:
        if random.random() <= p:
            x, y = self.img.size
            x_offset = random.uniform(x_offset_min, x_offset_max)
            y_offset = random.uniform(y_offset_min, y_offset_max)
            self._offset(int(x_offset * x), int(y_offset * y))

    @mark_augmentation
    def crop(
        self,
        p: float = 0.5,
        min_width: float = 0.5,
        max_width: float = 0.9,
        min_height: float = 0.5,
        max_height=0.9,
    ) -> None:
        if random.random() <= p:
            width, height = self.img.size
            crop_width = random.randint(int(min_width * width), int(max_width * width))
            crop_height = random.randint(int(min_height * height), int(max_height * height))
            x_min = random.randint(0, width - crop_width)
            y_min = random.randint(0, height - crop_height)
            x_max = x_min + crop_width
            y_max = y_min + crop_height
            self._crop(x_min, y_min, x_max, y_max)


if __name__ == "__main__":
    from pathlib import Path

    base_path = Path(__file__).parent
    image_path = base_path / "tests" / "alpaca.jpg"
    img = AugustImage(image_path)
    img.augment()
    img.show()
