import librosa
from pydub import AudioSegment
from pydub.playback import play
import random
import numpy as np
from numpy import ndarray
from audiomentations import (
    Compose,
    AddGaussianNoise,
    ApplyImpulseResponse,
    Shift,
    TimeMask,
    HighPassFilter,
    LowPassFilter,
    RoomSimulator
)


# TODO: add util to download echoes and implement impulse response
def impulse_response(y: ndarray, sr: int):
    convert = Compose([ApplyImpulseResponse()])
    return convert(samples=y, sample_rate=sr)


def _invert_polarity(y: ndarray) -> ndarray:
    return y * -1


def _time_stretch(y: ndarray, sr: int, factor: float) -> ndarray:
    return librosa.effects.time_stretch(y, rate=factor)


def time_shift(y: ndarray, sr: int, *, min_shift: float, max_shift: float, p: float) -> ndarray:
    convert = Compose([Shift(min_shift=min_shift, max_shift=max_shift, p=p)])
    y_new = convert(samples=y, sample_rate=sr)
    return y_new


def time_stretch(y: ndarray, sr: int, *, min_factor: float, max_factor: float, p: float) -> ndarray:
    if random.random() < p:
        factor = random.uniform(min_factor, max_factor)
        return _time_stretch(y, sr, factor=factor)
    return y


def invert_polarity(y: ndarray, sr: int, *, p: float) -> ndarray:
    if random.random() < p:
        return _invert_polarity(y)
    return y


def _pitch_scale(y: ndarray, sr: int, num_semitones: float) -> ndarray:
    return librosa.effects.pitch_shift(y, sr=sr, n_steps=num_semitones)


def pitch_scale(y: ndarray, sr: int, *, min_semitones: int, max_semitones: int, p: float) -> ndarray:
    if random.random() < p:
        num_semitones = random.randint(min_semitones, max_semitones)
        return _pitch_scale(y, sr, num_semitones=num_semitones)
    return y


def _gain(y: ndarray, factor: float) -> ndarray:
    return y * factor


def random_gain(y: ndarray, sr: int, *, min_factor: float, max_factor: float, p: float) -> ndarray:
    if random.random() < p:
        gain_rate = random.uniform(min_factor, max_factor)
        return _gain(y, gain_rate)
    return y


def gaussian_noise(y: ndarray, sr: int, *, min_amplitude: float, max_amplitude: float, p: float) -> ndarray:
    convert = Compose([AddGaussianNoise(min_amplitude=min_amplitude, max_amplitude=max_amplitude, p=p)])
    return convert(samples=y, sample_rate=sr)


def time_mask(y: ndarray, sr: int, *, min_part: float, max_part: float, p: float) -> ndarray:
    convert = Compose([TimeMask(min_band_part=min_part, max_band_part=max_part, p=p)])
    return convert(samples=y, sample_rate=sr)


def low_pass_filter(y: ndarray, sr: int, *, min_freq: float, max_freq: float, p: float) -> ndarray:
    convert = Compose([LowPassFilter(min_cutoff_freq=min_freq, max_cutoff_freq=max_freq, p=p)])
    return convert(y, sample_rate=sr)


def high_pass_filter(y: ndarray, sr: int, *, min_freq: float, max_freq: float, p: float) -> ndarray:
    convert = Compose([HighPassFilter(min_cutoff_freq=min_freq, max_cutoff_freq=max_freq, p=p)])
    return convert(y, sample_rate=sr)


def room(y: ndarray, sr: int, *, p: float) -> ndarray
    convert = Compose([RoomSimulator(p=p)])
    return convert(y, sample_rate=sr)


# https://youtu.be/bm1cQfb_pLA?si=8FGGSA3zPCxUseGJ


def librosa_play(y, sr):
    # convert from float to uint16
    temp = np.array(y * (1 << 15), dtype=np.int16)
    audio_segment = AudioSegment(
        temp.tobytes(), frame_rate=sr, sample_width=temp.dtype.itemsize, channels=1
    )
    play(audio_segment)
