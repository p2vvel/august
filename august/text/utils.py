import os

import nlpaug.augmenter.char as nac
import nlpaug.augmenter.word as naw
from nlpaug.util import DownloadUtil


def _download_models(dest_dir: str = ".", model: str = "fasttext") -> None:
    """
    Download pre-trained word embedding models.

    Args:
        dest_dir (str, optional): The directory where the models will be downloaded. Defaults to ".".
        model (str, optional): The name of the model to download (supports "fasttext", "word2vec", "glove").
                              Defaults to "fasttext".

    Raises:
        ValueError: If an unsupported model is specified.
    """
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    match model:
        case "fasttext":
            DownloadUtil.download_fasttext(model_name="wiki-news-300d-1M", dest_dir=dest_dir)
        case "word2vec":
            DownloadUtil.download_word2vec(dest_dir=dest_dir)
        case "glove":
            DownloadUtil.download_glove(model_name="glove.6B", dest_dir=dest_dir)
        case _:
            raise ValueError("Model value is unexpected. Only support fasttext, word2vec and glove.")


def synonym_replacement(text: str, *, p: float = 0.3, n: int = 1) -> str:
    """
    Replace n words in the sentence with synonyms from WordNet.

    Args:
        text (str): The input text to perform synonym replacement on.
        p (float, optional): The probability of performing synonym replacement. Defaults to 0.3.
        n (int, optional): The number of words to replace. Defaults to 1.

    Returns:
        str: The augmented text with synonym replacements.
    """
    aug = naw.SynonymAug(aug_p=p)
    augmented_text = aug.augment(text, n=n)
    return augmented_text


def antonym_replacement(text: str, *, p: float = 0.3, n: int = 1) -> str:
    """
    Replace n words in the sentence with antonyms.

    Args:
        text (str): The input text to perform antonym replacement on.
        p (float, optional): The probability of performing antonym replacement. Defaults to 0.3.
        n (int, optional): The number of words to replace. Defaults to 1.

    Returns:
        str: The augmented text with antonym replacements.
    """
    aug = naw.AntonymAug(aug_p=p)
    augmented_text = aug.augment(text, n=n)
    return augmented_text


def ocr(text: str, *, p: float = 0.3, n: int = 1):
    """
    Introduce OCR-style errors into the text.

    Args:
        text (str): The input text to apply OCR-style augmentation to.
        p (float, optional): The probability of introducing OCR errors. Defaults to 0.3.
        n (int, optional): The number of augmentations to apply. Defaults to 1.

    Returns:
        str: A list of augmented texts with OCR errors.
    """
    aug = nac.OcrAug(aug_char_p=p)
    augmented_texts = aug.augment(text, n=n)
    return augmented_texts


def keyboard(text: str, *, p: float = 0.3, n: int = 1):
    """
    Introduce keyboard typing errors into the text.

    Args:
        text (str): The input text to apply keyboard typing errors to.
        p (float, optional): The probability of introducing keyboard errors. Defaults to 0.3.
        n (int, optional): The number of augmentations to apply. Defaults to 1.

    Returns:
        str: A list of augmented texts with keyboard typing errors.
    """
    aug = nac.KeyboardAug(aug_char_p=p)
    augmented_texts = aug.augment(text, n=n)
    return augmented_texts


def random_char(text: str, *, p: float, n: int = 1):
    """
    Apply random character-level augmentation to the text.

    Args:
        text (str): The input text to be augmented.
        p (float): The probability of replacing characters.
        n (int, optional): The number of character replacements to perform. Defaults to 1.

    Returns:
        list[str]: A list of augmented texts with random character replacements.
    """
    aug = nac.RandomCharAug(aug_char_p=p)
    augmented_texts = aug.augment(text, n=n)
    return augmented_texts


def _random_word_aug(mode: str, text: str, *, p: float = 0.3, n: int = 1):
    """
    Apply word-based augmentation to the text using a specified mode.

    Args:
        mode (str): The augmentation mode (e.g., "delete," "substitute," "swap," "crop").
        text (str): The input text to be augmented.
        p (float, optional): The probability of performing the specified augmentation. Defaults to 0.3.
        n (int, optional): The number of augmentations to apply. Defaults to 1.

    Returns:
        list[str]: A list of augmented texts based on the specified word-based augmentation mode.
    """
    aug = naw.RandomWordAug(action=mode, aug_p=p)
    augmented_texts = aug.augment(text, n=n)
    return augmented_texts


def random_word_delete(text: str, *, p: float = 0.3, n: int = 1):
    """
    Delete random words from the input text.

    Args:
        text (str): The input text to be augmented.
        p (float, optional): The probability of word deletion. Defaults to 0.3.
        n (int, optional): The number of word deletions to perform. Defaults to 1.

    Returns:
        list[str]: A list of augmented texts with random word deletions.
    """
    return _random_word_aug("delete", text, p=p, n=n)


def random_word_substitute(text: str, *, p: float = 0.3, n: int = 1):
    """
    Substitute random words in the input text with synonyms or similar words.

    Args:
        text (str): The input text to be augmented.
        p (float, optional): The probability of word substitution. Defaults to 0.3.
        n (int, optional): The number of word substitutions to perform. Defaults to 1.

    Returns:
        list[str]: A list of augmented texts with random word substitutions.
    """
    return _random_word_aug("substitute", text, p=p, n=n)


def random_word_swap(text: str, *, p: float = 0.3, n: int = 1):
    """
    Swap positions of random words in the input text.

    Args:
        text (str): The input text to be augmented.
        p (float, optional): The probability of word swapping. Defaults to 0.3.
        n (int, optional): The number of word swaps to perform. Defaults to 1.

    Returns:
        list[str]: A list of augmented texts with random word swaps.
    """
    return _random_word_aug("swap", text, p=p, n=n)


def random_word_crop(text: str, *, p: float = 0.3, n: int = 1):
    """
    Crop random words from the input text.

    Args:
        text (str): The input text to be augmented.
        p (float, optional): The probability of word cropping. Defaults to 0.3.
        n (int, optional): The number of word crops to perform. Defaults to 1.

    Returns:
        list[str]: A list of augmented texts with random word cropping.
    """
    return _random_word_aug("crop", text, p=p, n=n)


def spelling(text: str, *, p: float = 0.3, n: int = 1):
    """
    Introduce spelling errors into the input text.

    Args:
        text (str): The input text to be augmented.
        p (float, optional): The probability of introducing spelling errors. Defaults to 0.3.
        n (int, optional): The number of spelling error augmentations to perform. Defaults to 1.

    Returns:
        list[str]: A list of augmented texts with spelling errors.
    """
    aug = naw.SpellingAug(aug_p=p)
    return aug.augment(text, n=n)


def embedding(text: str, n: int = 1):
    """
    Augment text by replacing words with semantically similar words from word embeddings.

    Args:
        text (str): The input text to be augmented.
        n (int, optional): The number of word embedding-based augmentations to perform. Defaults to 1.

    Returns:
        list[str]: A list of augmented texts with word embeddings-based substitutions.
    """
    aug = naw.WordEmbsAug(
        # model_type="word2vec", model_path="./models/GoogleNews-vectors-negative300.bin"
        model_type="fasttext",
        model_path="./models/wiki-news-300d-1M.vec",
    )
    augmented_texts = aug.augment(text, n=n)
    return augmented_texts


# shuffle sentences randomly
# exclude duplicates
