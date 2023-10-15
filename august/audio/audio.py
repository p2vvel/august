from pydub import AudioSegment


class AugustAudio:
    def __init__(self, filename: str):
        self.audio = AudioSegment.from_file(filename)

    

if __name__ == "__main__":
    pass