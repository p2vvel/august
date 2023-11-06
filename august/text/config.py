from pydantic import BaseModel, Field


class AugustTextConfig(BaseModel):
    synonym_replace_p: float = Field(0.3, text="Probability of synonym replacement", ge=0, le=1)
    antonym_replace_p: float = Field(0.3, text="Probability of antonym replacement", ge=0, le=1)
    ocr_p: float = Field(0.3, text="Probability of OCR distortion", ge=0, le=1)
    keyboard_p: float = Field(0.3, text="Probability of keyboard typos", ge=0, le=1)
    random_character_p: float = Field(0.3, text="Probability of random character insertion", ge=0, le=1)
    random_word_delete_p: float = Field(0.3, text="Probability of random word delete", ge=0, le=1)
    random_word_substitute_p: float = Field(
        0.3, text="Probability of random word substitute", ge=0, le=1
    )
    random_word_swap_p: float = Field(0.3, text="Probability of random word swap", ge=0, le=1)
    spelling_p: float = Field(0.3, text="Probability of misspelling ", ge=0, le=1)
