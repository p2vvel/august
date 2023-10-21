from pydub import AudioSegment
from pydub.playback import play
import random
import numpy as np
from audiomentations import (Compose, 
                             AddBackgroundNoise, 
                             AddShortNoises,
                             Shift
                             )

# Time shifting

def time_shift(y, sr):
    convert = Compose([Shift()])
    y_new = convert(samples=y, sample_rate=sr)
    return y_new

def time_stretch(y, sr, factor: float):
    new_y = librosa.effects.time_stretch(y, rate=factor)
    return new_y

def pitch_scale(signal, sr, num_semitones):
    return librosa.effects.pitch_shift(signal, sr=sr, n_steps=num_semitones)

def random_gain(signal, min_factor, max_factor):
    gain_rate = random.uniform(min_factor, max_factor)
    augmented_signal = signal * gain_rate
    return augmented_signal


def invert_polarity(signal):
    return signal * -1


# def reverb(y, sr):
    # return librosa.

# Noise addition
# Impulse response addition
# Filters
# Time masking
# Frequency masking
###### https://youtu.be/bm1cQfb_pLA?si=8FGGSA3zPCxUseGJ


def librosa_play(y, sr):
    # convert from float to uint16
    temp = np.array(y * (1<<15), dtype=np.int16)
    audio_segment = AudioSegment(
        temp.tobytes(), 
        frame_rate=sr,
        sample_width=temp.dtype.itemsize, 
        channels=1
    )
    play(audio_segment)

if __name__ == "__main__":
    path = "/home/pawel/august/august/audio/tests/resources/bff.m4a"
    
    from IPython.display import Audio

    import librosa
    y, sr = librosa.load(path)
    y = time_shift(y, sr)

    # y = time_stretch(y, sr, 0.6)
    # y = pitch_scale(y, sr, -3)
    # y = invert_polarity(y)
    # y = random_gain(y, min_factor=1.5, max_factor=2)

    # Audio(y, rate=sr)
    librosa_play(y, sr)