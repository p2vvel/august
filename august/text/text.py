from nlpaug.util import DownloadUtil
import os
import nlpaug.augmenter.char as nac
import nlpaug.augmenter.word as naw
import nlpaug.augmenter.sentence as nas
import nlpaug.flow as nafc

from nlpaug.util import Action


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
            raise ValueError(
                "Model value is unexpected. Only support fasttext, word2vec and glove."
            )


# synonym replacement
# Create a function that will take a string as an argument and replace words with their synonyms, using nlpAug library.
def synonym_replacement(text: str, n: int = 1) -> str:
    """
    Replace n words in the sentence with synonyms from wordnet.
    """
    aug = naw.SynonymAug()
    augmented_text = aug.augment(text, n=n)
    return augmented_text


def antonym_replacement(text: str, n: int = 1) -> str:
    """
    Replace n words in the sentence with antonyms
    """
    aug = naw.AntonymAug()
    augmented_text = aug.augment(text, n=n)
    return augmented_text


def ocr(text: str, n: int = 1):
    aug = nac.OcrAug()
    augmented_texts = aug.augment(text, n=n)
    return augmented_texts


def keyboard(text: str, n: int = 1):
    aug = nac.KeyboardAug()
    augmented_texts = aug.augment(text, n=n)
    return augmented_texts


def random_char(text: str, n: int = 1):
    aug = nac.RandomCharAug()
    augmented_texts = aug.augment(text, n=n)
    return augmented_texts


def _random_word_aug(mode: str, text: str, n: int):
    aug = naw.RandomWordAug(action=mode)
    augmented_texts = aug.augment(text, n=n)
    return augmented_texts


def random_word_delete(text: str, n: int = 1):
    return _random_word_aug("delete", text, n)


def random_word_substitute(text: str, n: int = 1):
    return _random_word_aug("substitute", text, n)


def random_word_swap(text: str, n: int = 1):
    return _random_word_aug("swap", text, n)


def random_word_crop(text: str, n: int = 1):
    return _random_word_aug("crop", text, n)


def spelling(text: str, n: int = 1):
    aug = naw.SpellingAug()
    augmented_texts = aug.augment(text, n=n)
    return augmented_texts


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


if __name__ == "__main__":
    # _download_models("models")

    text = "I love my little girl."
    text = "The good boy quick brown fox jumps over the lazy dog."

    print(text)
    print(antonym_replacement(text, n=10))

    # breakpoint()

    # print(synonym_replacement(text, n=5))
