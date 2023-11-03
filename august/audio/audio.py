from numpy import ndarray

from . import utils
import librosa


class AugustAudio:
    def __init__(self, audio_path: str) -> None:
        self.y: ndarray
        self.sr: int
        self.y, self.sr = librosa.load(audio_path)
        self.sr = int(self.sr)

    def time_shift(self, min_shift: float = -0.5, max_shift: float = 0.5, p: float = 0.5) -> None:
        self.y = utils.time_shift(self.y, self.sr, min_shift=min_shift, max_shift=max_shift, p=p)

    def time_stretch(self, min_factor: float = 0.5, max_factor: float = 1.5, p: float = 0.5) -> None:
        self.y = utils.time_stretch(self.y, self.sr, min_factor=min_factor, max_factor=max_factor, p=p)

    def invert_polarity(self, p: float = 0.5) -> None:
        self.y = utils.invert_polarity(self.y, self.sr, p=p)

    def pitch_scale(self, min_semitones: int = -6, max_semitones: int = 6, p: float = 0.5) -> None:
        self.y = utils.pitch_scale(
            self.y, self.sr, min_semitones=min_semitones, max_semitones=max_semitones, p=p
        )

    def random_gain(self, min_factor: float = 0.5, max_factor: float = 1.5, p: float = 0.5) -> None:
        self.y = utils.random_gain(self.y, self.sr, min_factor=min_factor, max_factor=max_factor, p=p)

    def gaussian_noise(
        self, min_amplitude: float = 0.001, max_amplitude: float = 0.015, p: float = 0.5
    ) -> None:
        self.y = utils.gaussian_noise(
            self.y, min_amplitude=min_amplitude, max_amplitude=max_amplitude, p=p
        )

    def time_mask(self, min_part: float = 0.01, max_part: float = 0.5, p: float = 0.5) -> None:
        self.y = utils.time_mask(self.y, self.sr, min_part=min_part, max_part=max_part, p=p)

    def low_pass_filter(self, min_freq: float = 150, max_freq: float = 7500, p: float = 0.5) -> None:
        self.y = utils.low_pass_filter(self.y, self.sr, min_freq=min_freq, max_freq=max_freq, p=p)

    def high_pass_filter(self, min_freq: float = 20, max_freq: float = 2400, p: float = 0.5) -> None:
        self.y = utils.high_pass_filter(self.y, self.sr, min_freq=min_freq, max_freq=max_freq, p=p)

    def room(self, p: float = 0.5) -> None:
        self.y = utils.room(self.y, self.sr, p=p)
