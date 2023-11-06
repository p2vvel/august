from pathlib import Path

from august.mixins import ExecuteAugmentationMixin
from august.text import utils
from august.text.config import AugustTextConfig
from august.text.decorators import AugustTextMark, mark_augmentation


class AugustText(ExecuteAugmentationMixin):
    """
    A class for text data augmentation using various augmentation methods.

    This class provides methods for augmenting text data with techniques like synonym replacement, antonym replacement,
    OCR-style modifications, keyboard typos, and more.

    Args:
        text (str): The input text to be augmented.
        config (AugustTextConfig, optional): Configuration settings for text augmentation. Defaults to AugustTextConfig().

    Attributes:
        text (str): The current text content.
        original_text (str): The original text content before any augmentations.
        config (AugustTextConfig): The configuration settings for text augmentation.
    """

    _augmentations = AugustTextMark.augmentations

    def __init__(self, text: str, config: AugustTextConfig = AugustTextConfig()) -> None:
        """
        Initialize the AugustText object.

        Args:
            text (str): The input text to be augmented.
            config (AugustTextConfig, optional): Configuration settings for text augmentation. Defaults to AugustTextConfig().
        """
        self.text = text
        self.original_text = text
        self.config = config

    def save(self, path: str | Path) -> None:
        """
        Save the augmented text to a file.

        Args:
            path (str or Path): The path to the file where the augmented text will be saved.
        """
        with open(path, "w") as f:
            f.write(self.text)

    @mark_augmentation
    def synonym_replace(self) -> None:
        """Replace words in the text with synonyms."""
        self.text = utils.synonym_replacement(self.text, p=self.config.synonym_replace_p)[0]

    @mark_augmentation
    def antonym_replace(self) -> None:
        """Replace words in the text with antonyms."""
        self.text = utils.antonym_replacement(self.text, p=self.config.antonym_replace_p)[0]

    @mark_augmentation
    def ocr(self) -> None:
        """Introduce OCR-style errors into the text."""
        self.text = utils.ocr(self.text, p=self.config.ocr_p)[0]

    @mark_augmentation
    def keyboard(self) -> None:
        """Introduce keyboard typing errors into the text."""
        self.text = utils.keyboard(self.text, p=self.config.keyboard_p)[0]

    @mark_augmentation
    def random_character(self) -> None:
        """Replace random characters in the text."""
        self.text = utils.random_char(self.text, p=self.config.random_character_p)[0]

    @mark_augmentation
    def random_word_delete(self) -> None:
        """Delete random words from the text."""
        self.text = utils.random_word_delete(self.text, p=self.config.random_word_delete_p)[0]

    @mark_augmentation
    def random_word_substitute(self) -> None:
        """Substitute random words in the text with synonyms or antonyms."""
        self.text = utils.random_word_substitute(self.text, p=self.config.random_word_substitute_p)[0]

    @mark_augmentation
    def random_word_swap(self) -> None:
        """Swap positions of random words in the text."""
        self.text = utils.random_word_swap(self.text, p=self.config.random_word_swap_p)[0]

    @mark_augmentation
    def spelling(self) -> None:
        """Introduce spelling errors into the text."""
        self.text = utils.spelling(self.text, p=self.config.spelling_p)[0]
