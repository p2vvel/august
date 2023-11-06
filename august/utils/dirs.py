import os
from typing import Iterable


def list_files_in_directory(directory):
    """List all files in a directory."""
    return list(filter(os.path.isfile, map(lambda x: os.path.join(directory, x), os.listdir(directory))))


def files_with_extensions(directory: str, allowed_extensions: Iterable[str]) -> list[str]:
    """List all images in a directory."""
    return list(filter(lambda x: x.endswith(allowed_extensions), list_files_in_directory(directory)))


def get_directory(directory: str):
    """Get directory, create if not exists."""
    if not os.path.exists(directory):
        os.makedirs(directory)
    return directory
