from pydub import AudioSegment
from pydub.playback import play

def jeopardy():
    sound = AudioSegment.from_file("../util/jeopardyTune.mp3")
    play(sound)

if __name__ == "__main__":
    jeopardy()