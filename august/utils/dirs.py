import os
from typing import Iterable


def list_files_in_directory(directory: str) -> list[str]:
    """
    List all files in a directory.

    Args:
        directory (str): The path to the directory to list files from.

    Returns:
        list[str]: A list of file paths in the specified directory.
    """
    return list(filter(os.path.isfile, map(lambda x: os.path.join(directory, x), os.listdir(directory))))


def files_with_extensions(directory: str, allowed_extensions: Iterable[str]) -> list[str]:
    """
    List all files with specific extensions in a directory.

    Args:
        directory (str): The path to the directory to search for files.
        allowed_extensions (Iterable[str]): A list of allowed file extensions to filter by.

    Returns:
        list[str]: A list of file paths with extensions specified in allowed_extensions.
    """
    return list(filter(lambda x: x.endswith(allowed_extensions), list_files_in_directory(directory)))


def get_directory(directory: str) -> str:
    """
    Get a directory and create it if it doesn't exist.

    Args:
        directory (str): The path to the directory to retrieve or create.

    Returns:
        str: The path to the directory. If it didn't exist before, it will be created.
    """
    if not os.path.exists(directory):
        os.makedirs(directory)
    return directory
