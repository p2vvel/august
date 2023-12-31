import random
from pathlib import Path

from PIL import Image as PILImage

from august.images.config import AugustImageConfig
from august.images.decorators import AugustImageMark, mark_augmentation
from august.images.mixins import AugustImageMixin
from august.mixins import ExecuteAugmentationMixin


class AugustImage(AugustImageMixin, ExecuteAugmentationMixin):
    """
    A class for augmenting and processing images using various augmentation methods.

    This class provides methods for augmenting images with techniques like mirroring, flipping,
    color changes, color temperature adjustments, rotation, blurring, offset, and cropping.

    Args:
        audio_path (str or Path): The path to the input image.
        config (AugustImageConfig, optional): Configuration settings for image augmentation. Defaults to AugustImageConfig().

    Attributes:
        img (PIL.Image.Image): The image loaded from the specified path.
        config (AugustImageConfig): The configuration settings for image augmentation.
    """

    _augmentations = AugustImageMark.augmentations

    def __init__(self, audio_path: str | Path, config: AugustImageConfig = AugustImageConfig()) -> None:
        """
        Initialize the AugustImage object.

        Args:
            audio_path (str or Path): The path to the input image.
            config (AugustImageConfig, optional): Configuration settings for image augmentation. Defaults to AugustImageConfig().
        """
        self.img = PILImage.open(audio_path)
        self.config = config

    def save(self, filename: str | Path) -> None:
        """
        Save the augmented image to a file.

        Args:
            filename (str or Path): The path to the file where the augmented image will be saved.
        """
        self.img.save(filename)

    def show(self, title: str | None = None) -> None:
        """
        Display the image in a viewer.

        Args:
            title (str or None, optional): The title for the displayed image. Defaults to None.
        """
        self.img.show(title=title)

    @mark_augmentation
    def mirror(self) -> None:
        """
        Apply mirroring to the image if the random probability is within the configured range.
        """
        if random.random() <= self.config.mirror_p:
            self._mirror()

    @mark_augmentation
    def flip(self) -> None:
        """
        Apply flipping to the image if the random probability is within the configured range.
        """
        if random.random() <= self.config.flip_p:
            self._flip()

    @mark_augmentation
    def color_change(self) -> None:
        """
        Apply color changes to the image if the random probability is within the configured range.
        """
        if random.random() <= self.config.color_p:
            color_foo = random.choice((self._sepia, self._black_and_white))
            color_foo()

    @mark_augmentation
    def color_temperature(self) -> None:
        """
        Adjust the color temperature of the image if the random probability is within the configured range.
        """
        if random.random() <= self.config.temperature_p:
            ratio = random.randint(self.config.min_temperature_ratio, self.config.max_temperature_ratio)
            self._color_temperature(ratio)

    @mark_augmentation
    def rotate(self) -> None:
        """
        Rotate the image by a random angle if the random probability is within the configured range.
        """
        if random.random() <= self.config.rotate_p:
            angle = random.randint(self.config.min_angle, self.config.max_angle)
            self._rotate(angle)

    @mark_augmentation
    def blur(self) -> None:
        """
        Apply blurring to the image if the random probability is within the configured range.
        """
        if random.random() <= self.config.blur_p:
            pixel_radius = random.randint(self.config.min_pixel_radius, self.config.max_pixel_radius)
            self._blur(pixel_radius)

    @mark_augmentation
    def offset(self) -> None:
        """
        Offset the image if the random probability is within the configured range.
        """
        if random.random() <= self.config.offset_p:
            x, y = self.img.size
            x_offset = random.uniform(self.config.min_x_offset, self.config.max_x_offset)
            y_offset = random.uniform(self.config.min_y_offset, self.config.max_y_offset)
            self._offset(int(x_offset * x), int(y_offset * y))

    @mark_augmentation
    def crop(self) -> None:
        """
        Crop a portion of the image if the random probability is within the configured range.
        """
        if random.random() <= self.config.crop_p:
            width, height = self.img.size
            min_width, max_width = self.config.min_x_crop, self.config.max_x_crop
            min_height, max_height = self.config.min_y_crop, self.config.max_y_crop
            crop_width = random.randint(int(min_width * width), int(max_width * width))
            crop_height = random.randint(int(min_height * height), int(max_height * height))
            x_min = random.randint(0, width - crop_width)
            y_min = random.randint(0, height - crop_height)
            x_max = x_min + crop_width
            y_max = y_min + crop_height
            self._crop(x_min, y_min, x_max, y_max)
