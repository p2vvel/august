import os

import nlpaug.augmenter.char as nac
import nlpaug.augmenter.word as naw
from nlpaug.util import DownloadUtil


def _download_models(dest_dir: str = ".", model: str = "fasttext") -> None:
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
    Replace n words in the sentence with synonyms from wordnet.
    """
    aug = naw.SynonymAug(aug_p=p)
    augmented_text = aug.augment(text, n=n)
    return augmented_text


def antonym_replacement(text: str, *, p: float = 0.3, n: int = 1) -> str:
    """
    Replace n words in the sentence with antonyms
    """
    aug = naw.AntonymAug(aug_p=p)
    augmented_text = aug.augment(text, n=n)
    return augmented_text


def ocr(text: str, *, p: float = 0.3, n: int = 1):
    aug = nac.OcrAug(aug_char_p=p)
    augmented_texts = aug.augment(text, n=n)
    return augmented_texts


def keyboard(text: str, *, p: float = 0.3, n: int = 1):
    aug = nac.KeyboardAug(aug_char_p=p)
    augmented_texts = aug.augment(text, n=n)
    return augmented_texts


def random_char(text: str, *, p: float, n: int = 1):
    aug = nac.RandomCharAug(aug_char_p=p)
    augmented_texts = aug.augment(text, n=n)
    return augmented_texts


def _random_word_aug(mode: str, text: str, *, p: float = 0.3, n: int = 1):
    aug = naw.RandomWordAug(action=mode, aug_p=p)
    augmented_texts = aug.augment(text, n=n)
    return augmented_texts


def random_word_delete(text: str, *, p: float = 0.3, n: int = 1):
    return _random_word_aug("delete", text, p=p, n=n)


def random_word_substitute(text: str, *, p: float = 0.3, n: int = 1):
    return _random_word_aug("substitute", text, p=p, n=n)


def random_word_swap(text: str, *, p: float = 0.3, n: int = 1):
    return _random_word_aug("swap", text, p=p, n=n)


def random_word_crop(text: str, *, p: float = 0.3, n: int = 1):
    return _random_word_aug("crop", text, p=p, n=n)


def spelling(text: str, *, p: float = 0.3, n: int = 1):
    aug = naw.SpellingAug(aug_p=p)
    return aug.augment(text, n=n)


def embedding(text: str, n: int = 1):
    aug = naw.WordEmbsAug(
        # model_type="word2vec", model_path="./models/GoogleNews-vectors-negative300.bin"
        model_type="fasttext",
        model_path="./models/wiki-news-300d-1M.vec",
    )
    augmented_texts = aug.augment(text, n=n)
    return augmented_texts


# shuffle sentences randomly
# exclude duplicates
