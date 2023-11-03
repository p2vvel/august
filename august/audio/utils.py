from pydub import AudioSegment
from pydub.playback import play
import random
import numpy as np
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

# Time shifting


def time_shift(y, sr):
    convert = Compose([Shift()])
    y_new = convert(samples=y, sample_rate=sr)
    return y_new


def _time_stretch(y, sr, factor: float):
    new_y = librosa.effects.time_stretch(y, rate=factor)
    return new_y


def _pitch_scale(signal, sr, num_semitones):
    return librosa.effects.pitch_shift(signal, sr=sr, n_steps=num_semitones)


def _random_gain(signal, min_factor, max_factor):
    gain_rate = random.uniform(min_factor, max_factor)
    augmented_signal = signal * gain_rate
    return augmented_signal


def invert_polarity(signal):
    return signal * -1


def gaussian_noise(signal, sr):
    convert = Compose([AddGaussianNoise()])
    y_new = convert(samples=signal, sample_rate=sr)
    return y_new


def impulse_response(signal, sr):
    convert = Compose([ApplyImpulseResponse()])
    y_new = convert(samples=signal, sample_rate=sr)
    return y_new


def time_mask(signal, sr):
    convert = Compose([TimeMask()])
    y_new = convert(samples=signal, sample_rate=sr)
    return y_new


def low_pass_filter(signal, sr):
    convert = Compose([LowPassFilter()])
    y_new = convert(signal, sample_rate=sr)
    return y_new


def high_pass_filter(signal, sr):
    convert = Compose([HighPassFilter()])
    y_new = convert(signal, sample_rate=sr)
    return y_new

def room(signal, sr):
    convert = Compose([RoomSimulator()])
    y_new = convert(signal, sample_rate=sr)
    return y_new



###### https://youtu.be/bm1cQfb_pLA?si=8FGGSA3zPCxUseGJ


def librosa_play(y, sr):
    # convert from float to uint16
    temp = np.array(y * (1 << 15), dtype=np.int16)
    audio_segment = AudioSegment(
        temp.tobytes(), frame_rate=sr, sample_width=temp.dtype.itemsize, channels=1
    )
    play(audio_segment)


if __name__ == "__main__":
    from pathlib import Path

    base_path = Path("C:\\Users\\p2vve\\PycharmProjects\\august\\august\\audio\\tests\\")
    path = base_path / "bff.m4a"


    import librosa

    y, sr = librosa.load(path)
    # y = time_shift(y, sr)
    y = room(y, sr)
    y = high_pass_filter(y, sr)

    # y = time_stretch(y, sr, 0.6)
    # y = pitch_scale(y, sr, -3)
    # y = invert_polarity(y)
    # y = random_gain(y, min_factor=1.5, max_factor=2)

    # Audio(y, rate=sr)
    librosa_play(y, sr)
