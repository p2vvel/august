from pydub import AudioSegment
from pydub.playback import play


class AugustAudio:
    def __init__(self, filename: str):
        self.audio: AudioSegment = AudioSegment.from_file(filename)

    def time_shift(self, endurance: int, t1: int, t2: int):
        a, b = sorted([t1, t2])
        t = min(endurance, b - a)
        self.audio = (
            self.audio[:a]
            + self.audio[b : b + t]
            + self.audio[a + t : b]
            + self.audio[a : a + t]
            + self.audio[b + t :]
        )
    
    def time_stretch(self, factor: float):
        # function to change audio speed without changing pitch
        # https://stackoverflow.com/questions/51434897/how-to-change-audio-speed-without-changing-pitch-with-ffmpeg
        self.audio = self.audio._spawn(
            self.audio.raw_data,
            overrides={
                "frame_rate": int(self.audio.frame_rate * factor)
            }
        )
        self.audio = self.audio.set_frame_rate(self.audio.frame_rate)


# Time shifting
# Time stretching
# Pitch scaling
# Noise addition
# Impulse response addition
# Filters
# Polarity Inversion
# Random gain
# Time masking
# Frequency masking
###### https://youtu.be/bm1cQfb_pLA?si=8FGGSA3zPCxUseGJ


if __name__ == "__main__":
    path = "/home/pawel/august/august/audio/tests/resources/bff.m4a"
    temp = AugustAudio(path)
    # AugustAudio.time_shift(temp, 5000, 0, 5000)
    AugustAudio.time_stretch(temp, 0.5)
    audio: AudioSegment = temp.audio


    play(audio)

    from pyrubberband import pyrb