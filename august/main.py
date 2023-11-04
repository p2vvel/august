from august.utils.dirs import images_in_directory


class August:
    def images(self, src: str, dest: str, n: int):
        images = images_in_directory(src)
        print("Image function", images)

    def audio(self):
        print("Audio function")

    def text(self):
        print("Text function")


if __name__ == "__main__":
    # fire.Fire(August)
    august = August()
    august.images("/home/pawel/Obrazy", "/home/pawel/Obrazy/augmented", 10)
