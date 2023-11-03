# tests here
from pixelmatch.contrib.PIL import pixelmatch
from ..images import AugustImage
from PIL import Image
from pathlib import Path


BASE_TEST_IMAGES_PATH = Path("august/images/tests/resources/")
FORMATS = ("jpg", "png")


def test_flip():
    for ext in FORMATS:
        transformed = AugustImage(BASE_TEST_IMAGES_PATH / ext / f"test_image.{ext}")
        transformed._flip()
        test_img = Image.open(BASE_TEST_IMAGES_PATH / ext / f"test_image_flip.{ext}")

        assert pixelmatch(transformed.img, test_img) == 0  # all pixels are exactly the same


def test_mirror():
    for ext in FORMATS:
        transformed = AugustImage(BASE_TEST_IMAGES_PATH / ext / f"test_image.{ext}")
        transformed._mirror()
        test_img = Image.open(BASE_TEST_IMAGES_PATH / ext / f"test_image_mirror.{ext}")

        assert pixelmatch(transformed.img, test_img) == 0


def test_blur():
    for ext in FORMATS:
        transformed = AugustImage(BASE_TEST_IMAGES_PATH / ext / f"test_image.{ext}")
        transformed._blur(3)
        test_img = Image.open(BASE_TEST_IMAGES_PATH / ext / f"test_image_blur.{ext}")

        assert pixelmatch(transformed.img, test_img) == 0  # all pixels are exactly the same


def test_bw():
    for ext in FORMATS:
        transformed = AugustImage(BASE_TEST_IMAGES_PATH / ext / f"test_image.{ext}")
        transformed._black_and_white()
        test_img = Image.open(BASE_TEST_IMAGES_PATH / ext / f"test_image_bw.{ext}")

        assert pixelmatch(transformed.img, test_img) == 0


def test_cold():
    for ext in FORMATS:
        transformed = AugustImage(BASE_TEST_IMAGES_PATH / ext / f"test_image.{ext}")
        transformed._color_temperature(-20)
        test_img = Image.open(BASE_TEST_IMAGES_PATH / ext / f"test_image_cold.{ext}")

        assert pixelmatch(transformed.img, test_img) == 0


def test_warm():
    for ext in FORMATS:
        transformed = AugustImage(BASE_TEST_IMAGES_PATH / ext / f"test_image.{ext}")
        transformed._color_temperature(20)
        test_img = Image.open(BASE_TEST_IMAGES_PATH / ext / f"test_image_warm.{ext}")

        assert pixelmatch(transformed.img, test_img) == 0


def test_crop():
    for ext in FORMATS:
        transformed = AugustImage(BASE_TEST_IMAGES_PATH / ext / f"test_image.{ext}")
        transformed._crop(50, 50, 250, 250)
        test_img = Image.open(BASE_TEST_IMAGES_PATH / ext / f"test_image_crop.{ext}")

        assert pixelmatch(transformed.img, test_img) == 0


def test_offset():
    for ext in FORMATS:
        transformed = AugustImage(BASE_TEST_IMAGES_PATH / ext / f"test_image.{ext}")
        transformed._offset(50, 50)
        test_img = Image.open(BASE_TEST_IMAGES_PATH / ext / f"test_image_offset.{ext}")

        assert pixelmatch(transformed.img, test_img) <= 10


def test_rotate():
    for ext in FORMATS:
        transformed = AugustImage(BASE_TEST_IMAGES_PATH / ext / f"test_image.{ext}")
        transformed._rotate(20)
        test_img = Image.open(BASE_TEST_IMAGES_PATH / ext / f"test_image_rotate.{ext}")

        assert pixelmatch(transformed.img, test_img) <= 100


def test_sepia():
    for ext in FORMATS:
        transformed = AugustImage(BASE_TEST_IMAGES_PATH / ext / f"test_image.{ext}")
        transformed._sepia()
        test_img = Image.open(BASE_TEST_IMAGES_PATH / ext / f"test_image_sepia.{ext}")

        assert pixelmatch(transformed.img, test_img) == 0
