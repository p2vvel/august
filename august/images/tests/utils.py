from august.images.image import AugustImage


def generate_test_images(base_path: str, ext: str):
    transforms = (
        AugustImage._mirror,
        AugustImage._flip,
        AugustImage._sepia,
        AugustImage._black_and_white,
        # AugustImage._color_temperature,
        # AugustImage.rotate,
        # AugustImage.noise,
        # AugustImage.blur,
        # AugustImage.crop,
        # AugustImage.offset,
    )

    for name, trans in zip(("mirror", "flip", "sepia", "bw"), transforms):
        temp = AugustImage(base_path + f"/{ext}/test_image.{ext}")
        trans(temp)
        temp.save(base_path + f"/{ext}/test_image_{name}.{ext}")
        
    # warm
    temp = AugustImage(base_path + f"/{ext}/test_image.{ext}")
    AugustImage._color_temperature(temp, 20)
    temp.save(base_path + f"/{ext}/test_image_warm.{ext}")
    # cold
    temp = AugustImage(base_path + f"/{ext}/test_image.{ext}")
    AugustImage._color_temperature(temp, -20)
    temp.save(base_path + f"/{ext}/test_image_cold.{ext}")
    # rotated
    temp = AugustImage(base_path + f"/{ext}/test_image.{ext}")
    AugustImage._rotate(temp, 20)
    temp.save(base_path + f"/{ext}/test_image_rotate.{ext}")
    # blur
    temp = AugustImage(base_path + f"/{ext}/test_image.{ext}")
    AugustImage._blur(temp, 3)
    temp.save(base_path + f"/{ext}/test_image_blur.{ext}")
    # crop
    temp = AugustImage(base_path + f"/{ext}/test_image.{ext}")
    AugustImage._crop(temp, 50, 50, 250, 250)
    temp.save(base_path + f"/{ext}/test_image_crop.{ext}")
    # offset
    temp = AugustImage(base_path + f"/{ext}/test_image.{ext}")
    AugustImage._offset(temp, 50, 50)
    temp.save(base_path + f"/{ext}/test_image_offset.{ext}")

if __name__ == "__main__":
    base_path = "/home/pawel/august/august/images/tests/resources"
    generate_test_images(base_path, "png")
    generate_test_images(base_path, "jpg")