import random

import librosa
import numpy as np
from audiomentations import (
    AddGaussianNoise,
    ApplyImpulseResponse,
    Compose,
    HighPassFilter,
    LowPassFilter,
    RoomSimulator,
    Shift,
    TimeMask,
)
from numpy import ndarray
from pydub import AudioSegment
from pydub.playback import play


# TODO: add util to download echoes and implement impulse response
def impulse_response(y: ndarray, sr: int):
    """
    Apply impulse response augmentation to the audio.

    Args:
        y (ndarray): The audio waveform.
        sr (int): The sample rate of the audio.

    Returns:
        ndarray: The augmented audio waveform.
    """
    convert = Compose([ApplyImpulseResponse()])
    return convert(samples=y, sample_rate=sr)


def _invert_polarity(y: ndarray) -> ndarray:
    """
    Invert the polarity of the audio.

    Args:
        y (ndarray): The audio waveform.

    Returns:
        ndarray: The audio waveform with inverted polarity.
    """
    return y * -1


def _time_stretch(y: ndarray, sr: int, factor: float) -> ndarray:
    """
    Apply time stretching to the audio.

    Args:
        y (ndarray): The audio waveform.
        sr (int): The sample rate of the audio.
        factor (float): The time stretch factor.

    Returns:
        ndarray: The time-stretched audio waveform.
    """
    return librosa.effects.time_stretch(y, rate=factor)


def time_shift(y: ndarray, sr: int, *, min_shift: float, max_shift: float, p: float) -> ndarray:
    """
    Apply time shifting to the audio if the random probability is within the configured range.

    Args:
        y (ndarray): The audio waveform.
        sr (int): The sample rate of the audio.
        min_shift (float): The minimum time shift in seconds.
        max_shift (float): The maximum time shift in seconds.
        p (float): The probability of applying time shift.

    Returns:
        ndarray: The audio waveform with time shift applied.
    """
    convert = Compose([Shift(min_shift=min_shift, max_shift=max_shift, p=p)])
    y_new = convert(samples=y, sample_rate=sr)
    return y_new


def time_stretch(y: ndarray, sr: int, *, min_factor: float, max_factor: float, p: float) -> ndarray:
    """
    Apply time stretching to the audio.

    Args:
        y (ndarray): The audio waveform.
        sr (int): The sample rate of the audio.
        min_factor (float): The minimum time stretching factor.
        max_factor (float): The maximum time stretching factor.
        p (float): The probability of applying time stretching.

    Returns:
        ndarray: The audio waveform with time stretching applied if the condition is met, otherwise the original audio.
    """
    if random.random() < p:
        factor = random.uniform(min_factor, max_factor)
        return _time_stretch(y, sr, factor=factor)
    return y


def invert_polarity(y: ndarray, sr: int, *, p: float) -> ndarray:
    """
    Invert the polarity of the audio if the random probability is within the specified range.

    Args:
        y (ndarray): The audio waveform.
        sr (int): The sample rate of the audio.
        p (float): The probability of inverting polarity.

    Returns:
        ndarray: The audio waveform with inverted polarity if the condition is met, otherwise the original audio.
    """
    if random.random() < p:
        return _invert_polarity(y)
    return y


def _pitch_scale(y: ndarray, sr: int, num_semitones: float) -> ndarray:
    """
    Apply pitch scaling to the audio.

    Args:
        y (ndarray): The audio waveform.
        sr (int): The sample rate of the audio.
        num_semitones (float): The number of semitones to shift the pitch.

    Returns:
        ndarray: The audio waveform with pitch scaling applied.
    """
    return librosa.effects.pitch_shift(y, sr=sr, n_steps=num_semitones)


def pitch_scale(y: ndarray, sr: int, *, min_semitones: int, max_semitones: int, p: float) -> ndarray:
    """
    Apply pitch scaling to the audio if the random probability is within the specified range.

    Args:
        y (ndarray): The audio waveform.
        sr (int): The sample rate of the audio.
        min_semitones (int): The minimum number of semitones for pitch scaling.
        max_semitones (int): The maximum number of semitones for pitch scaling.
        p (float): The probability of applying pitch scaling.

    Returns:
        ndarray: The audio waveform with pitch scaling applied if the condition is met, otherwise the original audio.
    """
    if random.random() < p:
        num_semitones = random.randint(min_semitones, max_semitones)
        return _pitch_scale(y, sr, num_semitones=num_semitones)
    return y


def _gain(y: ndarray, factor: float) -> ndarray:
    """
    Apply gain adjustment to the audio.

    Args:
        y (ndarray): The audio waveform.
        factor (float): The gain adjustment factor.

    Returns:
        ndarray: The audio waveform with gain adjustment applied.
    """
    return y * factor


def random_gain(y: ndarray, sr: int, *, min_factor: float, max_factor: float, p: float) -> ndarray:
    """
    Apply random gain adjustment to the audio if the random probability is within the specified range.

    Args:
        y (ndarray): The audio waveform.
        sr (int): The sample rate of the audio.
        min_factor (float): The minimum gain adjustment factor.
        max_factor (float): The maximum gain adjustment factor.
        p (float): The probability of applying gain adjustment.

    Returns:
        ndarray: The audio waveform with gain adjustment applied if the condition is met, otherwise the original audio.
    """
    if random.random() < p:
        gain_rate = random.uniform(min_factor, max_factor)
        return _gain(y, gain_rate)
    return y


def gaussian_noise(
    y: ndarray, sr: int, *, min_amplitude: float, max_amplitude: float, p: float
) -> ndarray:
    """
    Apply Gaussian noise to the audio.

    Args:
        y (ndarray): The audio waveform.
        sr (int): The sample rate of the audio.
        min_amplitude (float): The minimum amplitude of Gaussian noise.
        max_amplitude (float): The maximum amplitude of Gaussian noise.
        p (float): The probability of applying Gaussian noise.

    Returns:
        ndarray: The audio waveform with Gaussian noise applied if the condition is met, otherwise the original audio.
    """
    convert = Compose([AddGaussianNoise(min_amplitude=min_amplitude, max_amplitude=max_amplitude, p=p)])
    return convert(samples=y, sample_rate=sr)


def time_mask(y: ndarray, sr: int, *, min_part: float, max_part: float, p: float) -> ndarray:
    """
    Apply time masking to the audio.

    Args:
        y (ndarray): The audio waveform.
        sr (int): The sample rate of the audio.
        min_part (float): The minimum duration of time masking.
        max_part (float): The maximum duration of time masking.
        p (float): The probability of applying time masking.

    Returns:
        ndarray: The audio waveform with time masking applied if the condition is met, otherwise the original audio.
    """
    convert = Compose([TimeMask(min_band_part=min_part, max_band_part=max_part, p=p)])
    return convert(samples=y, sample_rate=sr)


def low_pass_filter(y: ndarray, sr: int, *, min_freq: float, max_freq: float, p: float) -> ndarray:
    """
    Apply low-pass filtering to the audio.

    Args:
        y (ndarray): The audio waveform.
        sr (int): The sample rate of the audio.
        min_freq (float): The minimum cutoff frequency for low-pass filtering.
        max_freq (float): The maximum cutoff frequency for low-pass filtering.
        p (float): The probability of applying low-pass filtering.

    Returns:
        ndarray: The audio waveform with low-pass filtering applied if the condition is met, otherwise the original audio.
    """
    convert = Compose([LowPassFilter(min_cutoff_freq=min_freq, max_cutoff_freq=max_freq, p=p)])
    return convert(y, sample_rate=sr)


def high_pass_filter(y: ndarray, sr: int, *, min_freq: float, max_freq: float, p: float) -> ndarray:
    """
    Apply high-pass filtering to the audio.

    Args:
        y (ndarray): The audio waveform.
        sr (int): The sample rate of the audio.
        min_freq (float): The minimum cutoff frequency for high-pass filtering.
        max_freq (float): The maximum cutoff frequency for high-pass filtering.
        p (float): The probability of applying high-pass filtering.

    Returns:
        ndarray: The audio waveform with high-pass filtering applied if the condition is met, otherwise the original audio.
    """
    convert = Compose([HighPassFilter(min_cutoff_freq=min_freq, max_cutoff_freq=max_freq, p=p)])
    return convert(y, sample_rate=sr)


def room(y: ndarray, sr: int, *, p: float) -> ndarray:
    """
    Apply room simulation to the audio.

    Args:
        y (ndarray): The audio waveform.
        sr (int): The sample rate of the audio.
        p (float): The probability of applying room simulation.

    Returns:
        ndarray: The audio waveform with room simulation applied if the condition is met, otherwise the original audio.
    """
    convert = Compose([RoomSimulator(p=p)])
    return convert(y, sample_rate=sr)


# https://youtu.be/bm1cQfb_pLA?si=8FGGSA3zPCxUseGJ


def librosa_play(y, sr):
    """
    Play the audio using the PyDub library.

    Args:
        y: The audio waveform.
        sr: The sample rate of the audio.

    Returns:
        None
    """
    # convert from float to uint16
    temp = np.array(y * (1 << 15), dtype=np.int16)
    audio_segment = AudioSegment(
        temp.tobytes(), frame_rate=sr, sample_width=temp.dtype.itemsize, channels=1
    )
    play(audio_segment)
