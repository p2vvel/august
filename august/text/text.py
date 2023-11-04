from august.text import utils


class AugustText:
    def __init__(self, text: str) -> None:
        self.text = text
        self.original_text = text

    def synonym_replace(self, p: float = 0.3) -> None:
        self.text = utils.synonym_replacement(self.text, p=p)

    def antonym_replace(self, p: float = 0.3) -> None:
        self.text = utils.antonym_replacement(self.text, p=p)

    def ocr(self, p: float = 0.3) -> None:
        self.text = utils.ocr(self.text, p=p)

    def keyboard(self, p: float = 0.3) -> None:
        self.text = utils.keyboard(self.text, p=p)

    def random_character(self, p: float = 0.3) -> None:
        self.text = utils.random_char(self.text, p=p)

    def random_word_delete(self, p: float = 0.3) -> None:
        self.text = utils.random_word_delete(self.text, p=p)

    def random_word_substitute(self, p: float = 0.3) -> None:
        self.text = utils.random_word_substitute(self.text, p=p)

    def random_word_swap(self, p: float = 0.3) -> None:
        self.text = utils.random_word_swap(self.text, p=p)

    def spelling(self, p: float = 0.3) -> None:
        self.text = utils.spelling(self.text, p=p)


if __name__ == "__main__":
    text = "The quick brown fox jumps over the lazy dog"

    aug = AugustText(text)
    aug.synonym_replace()
    aug.antonym_replace()
    # aug.ocr()
    # aug.keyboard()
    # aug.random_character()
    aug.random_word_delete()
    # aug.random_word_substitute()
    aug.random_word_swap()
    # aug.spelling()

    print(aug.text)
