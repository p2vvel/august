from . import utils
import librosa
import random


class AugustAudio:
    def __init__(self, audio_path: str):
        self.y, self.sr = librosa.load(audio_path)
