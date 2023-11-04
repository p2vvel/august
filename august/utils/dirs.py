import os


def list_files_in_directory(directory):
    """List all files in a directory."""
    return list(filter(os.path.isfile, map(lambda x: os.path.join(directory, x), os.listdir(directory))))


def images_in_directory(directory: str) -> list[str]:
    """List all images in a directory."""
    allowed_extensions = (".jpg", ".jpeg", ".png")
    return list(filter(lambda x: x.endswith(allowed_extensions), list_files_in_directory(directory)))


def get_directory(directory: str):
    """Get directory, create if not exists."""
    if not os.path.exists(directory):
        os.makedirs(directory)
    return directory


if __name__ == "__main__":
    pass
    files = images_in_directory("/home/pawel/Obrazy/temp")
    print(len(files), files)
