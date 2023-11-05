from pathlib import Path

from august.images.images import AugustImage
from august.utils.dirs import get_directory, images_in_directory


class August:
    def images(self, source: str, destination: str, n: int):
        dest_path = Path(get_directory(destination))
        images = images_in_directory(source)
        for img in images:
            img_path = Path(img)
            print("IMG: ", img_path)
            aug_img = AugustImage(img_path)
            aug_img.save(dest_path / ("aug_" + img_path.name))
        # print("Image function", images, dest)

    def audio(self):
        print("Audio function")

    def text(self):
        print("Text function")


if __name__ == "__main__":
    # fire.Fire(August)
    august = August()
    august.images("/home/pawel/Obrazy/temp", "/home/pawel/Obrazy/augmented", 10)
