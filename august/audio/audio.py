from pathlib import Path

import librosa
import soundfile as sf
from numpy import ndarray

from august.audio import utils
from august.audio.config import AugustAudioConfig
from august.audio.decorators import AugustAudioMark, mark_augmentation
from august.mixins import ExecuteAugmentationMixin


class AugustAudio(ExecuteAugmentationMixin):
    """
    A class for augmenting and processing audio using various augmentation methods.

    This class provides methods for augmenting audio, such as time shifting, time stretching,
    polarity inversion, pitch scaling, gain adjustments, adding noise, applying time masking,
    and filtering (low-pass and high-pass).

    Args:
        audio_path (str or Path): The path to the input audio file.
        config (AugustAudioConfig, optional): Configuration settings for audio augmentation. Defaults to AugustAudioConfig().

    Attributes:
        y (ndarray): The audio waveform.
        sr (int): The sample rate of the audio.
        config (AugustAudioConfig): The configuration settings for audio augmentation.
    """

    _augmentations = AugustAudioMark.augmentations

    def __init__(self, audio_path: str | Path, config: AugustAudioConfig = AugustAudioConfig()) -> None:
        """
        Initialize the AugustAudio object.

        Args:
            audio_path (str or Path): The path to the input audio file.
            config (AugustAudioConfig, optional): Configuration settings for audio augmentation. Defaults to AugustAudioConfig().
        """
        self.y: ndarray
        self.sr: int
        self.y, self.sr = librosa.load(audio_path)
        self.sr = int(self.sr)
        self.config = config

    def save(self, filename: str | Path, format: str = "wav") -> None:
        """
        Save the augmented audio to a file.

        Args:
            filename (str or Path): The path to the file where the augmented audio will be saved.
            format (str, optional): The file format to use for saving the audio. Defaults to "wav".
        """
        sf.write(filename, data=self.y, samplerate=self.sr, format=format)

    @mark_augmentation
    def time_shift(self) -> None:
        """
        Apply time shifting to the audio if the random probability is within the configured range.
        """
        p = self.config.time_shift_p
        min_shift, max_shift = self.config.min_shift, self.config.max_shift
        self.y = utils.time_shift(self.y, self.sr, min_shift=min_shift, max_shift=max_shift, p=p)

    @mark_augmentation
    def time_stretch(self) -> None:
        """
        Apply time stretching to the audio if the random probability is within the configured range.
        """
        p = self.config.time_stretch_p
        min_factor, max_factor = self.config.min_stretch_factor, self.config.max_stretch_factor
        self.y = utils.time_stretch(self.y, self.sr, min_factor=min_factor, max_factor=max_factor, p=p)

    @mark_augmentation
    def invert_polarity(self) -> None:
        """
        Invert the polarity of the audio if the random probability is within the configured range.
        """
        p = self.config.invert_polarity_p
        self.y = utils.invert_polarity(self.y, self.sr, p=p)

    @mark_augmentation
    def pitch_scale(self) -> None:
        """
        Apply pitch scaling to the audio if the random probability is within the configured range.
        """
        p = self.config.pitch_scale_p
        min_semitones, max_semitones = self.config.min_semitones, self.config.max_semitones
        self.y = utils.pitch_scale(
            self.y, self.sr, min_semitones=min_semitones, max_semitones=max_semitones, p=p
        )

    @mark_augmentation
    def random_gain(self) -> None:
        """
        Apply random gain adjustments to the audio if the random probability is within the configured range.
        """
        p = self.config.random_gain_p
        min_factor, max_factor = self.config.min_gain_factor, self.config.max_gain_factor
        self.y = utils.random_gain(self.y, self.sr, min_factor=min_factor, max_factor=max_factor, p=p)

    @mark_augmentation
    def gaussian_noise(self) -> None:
        """
        Add Gaussian noise to the audio if the random probability is within the configured range.
        """
        p = self.config.gaussian_noise_p
        min_amplitude, max_amplitude = self.config.min_gain_amplitude, self.config.max_gain_amplitude
        self.y = utils.gaussian_noise(
            self.y, self.sr, min_amplitude=min_amplitude, max_amplitude=max_amplitude, p=p
        )

    @mark_augmentation
    def time_mask(self) -> None:
        """
        Apply time masking to the audio if the random probability is within the configured range.
        """
        p = self.config.time_mask_p
        min_part, max_part = self.config.min_mask_part, self.config.max_mask_part
        self.y = utils.time_mask(self.y, self.sr, min_part=min_part, max_part=max_part, p=p)

    @mark_augmentation
    def low_pass_filter(self) -> None:
        """
        Apply a low-pass filter to the audio if the random probability is within the configured range.
        """
        p = self.config.low_pass_filter_p
        min_freq, max_freq = self.config.min_low_pass_freq, self.config.max_low_pass_freq
        self.y = utils.low_pass_filter(self.y, self.sr, min_freq=min_freq, max_freq=max_freq, p=p)

    @mark_augmentation
    def high_pass_filter(self) -> None:
        """
        Apply a high-pass filter to the audio if the random probability is within the configured range.
        """
        p = self.config.high_pass_filter_p
        min_freq, max_freq = self.config.min_high_pass_freq, self.config.max_high_pass_freq
        self.y = utils.high_pass_filter(self.y, self.sr, min_freq=min_freq, max_freq=max_freq, p=p)

    @mark_augmentation
    def room(self) -> None:
        """
        Apply room simulation to the audio if the random probability is within the configured range.
        """
        p = self.config.room_p
        self.y = utils.room(self.y, self.sr, p=p)
