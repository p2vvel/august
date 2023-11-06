from PIL import Image as PILImage
from PIL import ImageChops, ImageFilter, ImageOps

from . import utils


class AugustImageMixin:
    """
    A mixin class for image augmentation methods.

    This mixin provides various image augmentation methods, such as mirroring, flipping, color adjustments,
    rotation, blurring, cropping, and more.

    Attributes:
        img (PIL.Image.Image): The image to be augmented.
    """

    def _mirror(self) -> None:
        """
        Mirror the image horizontally (left to right).
        """
        self.img = self.img.transpose(PILImage.FLIP_LEFT_RIGHT)

    def _flip(self) -> None:
        """
        Flip the image vertically (top to bottom).
        """
        self.img = self.img.transpose(PILImage.FLIP_TOP_BOTTOM)

    def _sepia(self) -> None:
        """
        Apply a sepia filter to the image.
        """
        self.img = utils.sepia(self.img)

    def _black_and_white(self) -> None:
        """
        Convert the image to black and white (grayscale).
        """
        self.img = ImageOps.grayscale(self.img.convert("RGB"))

    def _color_temperature(self, ratio: int) -> None:
        """
        Adjust the color temperature of the image.

        Args:
            ratio (int): The ratio to adjust the color temperature.
        """
        self.img = utils.change_warmth(self.img, ratio)

    def _rotate(self, angle: float, expand: bool = False) -> None:
        """
        Rotate the image by a specified angle.

        Args:
            angle (float): The angle in degrees to rotate the image.
            expand (bool, optional): Whether to expand the image canvas to fit the rotated image. Defaults to False.
        """
        self.img = self.img.rotate(angle=angle, expand=expand)

    def _noise(self) -> None:
        """
        Apply noise to the image (not implemented).
        """
        pass

    def _blur(self, pixel_radius: int) -> None:
        """
        Apply a box blur filter to the image.

        Args:
            pixel_radius (int): The pixel radius for the blur filter.
        """
        self.img = self.img.filter(ImageFilter.BoxBlur(pixel_radius))

    def _crop(self, x_min: int, y_min: int, x_max: int, y_max: int) -> None:
        """
        Crop a rectangular region from the image.

        Args:
            x_min (int): The minimum X-coordinate of the cropping region.
            y_min (int): The minimum Y-coordinate of the cropping region.
            x_max (int): The maximum X-coordinate of the cropping region.
            y_max (int): The maximum Y-coordinate of the cropping region.
        """
        self.img = self.img.crop((x_min, y_min, x_max, y_max))

    def _offset(self, x_offset: int, y_offset: int) -> None:
        """
        Offset the image by a specified number of pixels in the X and Y directions.

        Args:
            x_offset (int): The offset value in the X direction.
            y_offset (int): The offset value in the Y direction.
        """
        self.img = ImageChops.offset(self.img, x_offset, y_offset)
