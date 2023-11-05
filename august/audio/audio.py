from pathlib import Path

import librosa
from numpy import ndarray

from august.audio import utils
from august.audio.config import AugustAudioConfig
from august.audio.decorators import AugustAudioMark, mark_augmentation
from august.mixins import ExecuteAugmentationMixin


class AugustAudio(ExecuteAugmentationMixin):
    _augmentations = AugustAudioMark.augmentations

    def __init__(self, audio_path: str | Path, config: AugustAudioConfig = AugustAudioConfig()) -> None:
        self.y: ndarray
        self.sr: int
        self.y, self.sr = librosa.load(audio_path)
        self.sr = int(self.sr)
        self.config = config

    @mark_augmentation
    def time_shift(self) -> None:
        p = self.config.time_shift_p
        min_shift, max_shift = self.config.min_shift, self.config.max_shift
        self.y = utils.time_shift(self.y, self.sr, min_shift=min_shift, max_shift=max_shift, p=p)

    @mark_augmentation
    def time_stretch(self) -> None:
        p = self.config.time_stretch_p
        min_factor, max_factor = self.config.min_stretch_factor, self.config.max_stretch_factor
        self.y = utils.time_stretch(self.y, self.sr, min_factor=min_factor, max_factor=max_factor, p=p)

    @mark_augmentation
    def invert_polarity(self) -> None:
        p = self.config.invert_polarity_p
        self.y = utils.invert_polarity(self.y, self.sr, p=p)

    @mark_augmentation
    def pitch_scale(self) -> None:
        p = self.config.pitch_scale_p
        min_semitones, max_semitones = self.config.min_semitones, self.config.max_semitones
        self.y = utils.pitch_scale(
            self.y, self.sr, min_semitones=min_semitones, max_semitones=max_semitones, p=p
        )

    @mark_augmentation
    def random_gain(self) -> None:
        p = self.config.random_gain_p
        min_factor, max_factor = self.config.min_gain_factor, self.config.max_gain_factor
        self.y = utils.random_gain(self.y, self.sr, min_factor=min_factor, max_factor=max_factor, p=p)

    @mark_augmentation
    def gaussian_noise(self) -> None:
        p = self.config.gaussian_noise_p
        min_amplitude, max_amplitude = self.config.min_gain_amplitude, self.config.max_gain_amplitude
        self.y = utils.gaussian_noise(
            self.y, self.sr, min_amplitude=min_amplitude, max_amplitude=max_amplitude, p=p
        )

    @mark_augmentation
    def time_mask(self) -> None:
        p = self.config.time_mask_p
        min_part, max_part = self.config.min_mask_part, self.config.max_mask_part
        self.y = utils.time_mask(self.y, self.sr, min_part=min_part, max_part=max_part, p=p)

    @mark_augmentation
    def low_pass_filter(self) -> None:
        p = self.config.low_pass_filter_p
        min_freq, max_freq = self.config.min_low_pass_freq, self.config.max_low_pass_freq
        self.y = utils.low_pass_filter(self.y, self.sr, min_freq=min_freq, max_freq=max_freq, p=p)

    @mark_augmentation
    def high_pass_filter(self) -> None:
        p = self.config.high_pass_filter_p
        min_freq, max_freq = self.config.min_high_pass_freq, self.config.max_high_pass_freq
        self.y = utils.high_pass_filter(self.y, self.sr, min_freq=min_freq, max_freq=max_freq, p=p)

    @mark_augmentation
    def room(self) -> None:
        p = self.config.room_p
        self.y = utils.room(self.y, self.sr, p=p)


if __name__ == "__main__":
    from pathlib import Path

    base_path = Path(__file__).parent
    audio_path = base_path / "tests" / "bff.m4a"
    audio = AugustAudio(audio_path)
    audio.augment()
    # audio.time_shift(p=1)
    # audio.time_stretch(p=1)
    # audio.invert_polarity(p=1)
    # audio.pitch_scale(p=1)
    # audio.random_gain(p=1)
    # audio.gaussian_noise(p=1)
    # audio.time_mask(p=1)
    # audio.low_pass_filter(p=1)
    # audio.high_pass_filter(p=1)
    # audio.room(p=1)

    utils.librosa_play(audio.y, audio.sr)
    # sf.write("augmented.wav", audio.y, audio.sr)
