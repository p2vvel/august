from pathlib import Path

from august.mixins import ExecuteAugmentationMixin
from august.text import utils
from august.text.config import AugustTextConfig
from august.text.decorators import AugustTextMark, mark_augmentation


class AugustText(ExecuteAugmentationMixin):
    _augmentations = AugustTextMark.augmentations

    def __init__(self, text: str, config: AugustTextConfig = AugustTextConfig()) -> None:
        self.text = text
        self.original_text = text
        self.config = config

    def save(self, path: str | Path) -> None:
        with open(path, "w") as f:
            f.write(self.text)

    @mark_augmentation
    def synonym_replace(self) -> None:
        self.text = utils.synonym_replacement(self.text, p=self.config.synonym_replace_p)[0]

    @mark_augmentation
    def antonym_replace(self) -> None:
        self.text = utils.antonym_replacement(self.text, p=self.config.antonym_replace_p)[0]

    @mark_augmentation
    def ocr(self) -> None:
        self.text = utils.ocr(self.text, p=self.config.ocr_p)[0]

    @mark_augmentation
    def keyboard(self) -> None:
        self.text = utils.keyboard(self.text, p=self.config.keyboard_p)[0]

    @mark_augmentation
    def random_character(self) -> None:
        self.text = utils.random_char(self.text, p=self.config.random_character_p)[0]

    @mark_augmentation
    def random_word_delete(self) -> None:
        self.text = utils.random_word_delete(self.text, p=self.config.random_word_delete_p)[0]

    @mark_augmentation
    def random_word_substitute(self) -> None:
        self.text = utils.random_word_substitute(self.text, p=self.config.random_word_substitute_p)[0]

    @mark_augmentation
    def random_word_swap(self) -> None:
        self.text = utils.random_word_swap(self.text, p=self.config.random_word_swap_p)[0]

    @mark_augmentation
    def spelling(self) -> None:
        self.text = utils.spelling(self.text, p=self.config.spelling_p)[0]
