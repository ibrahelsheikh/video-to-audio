import wave, math, contextlib
import speech_recognition as sr
from moviepy.editor import AudioFileClip

transcribed_audio_file_name = "transcribed_speech.wav"
file_name = "D:\\music\\Marshmello.mp4"

audioclip = AudioFileClip(file_name)
audioclip.write_audiofile(transcribed_audio_file_name)

with contextlib.closing(wave.open(transcribed_audio_file_name, 'r')) as f:
    frames = f.getnframes()
    rate = f.getframerate()
    duration = frames / float(rate)

total_duration = math.ceil(duration / 60)
r = sr.Recognizer()

for i in range(0, total_duration):
    with sr.AudioFile(transcribed_audio_file_name) as source:
        audio = r.record(source, offset=i * 60, duration=60)
    f = open("transcription.txt", "a")

    try:
        output = r.recognize_google(audio, language="en-US")
        f.write(output)
        print(output)

    except sr.UnknownValueError:
        f.write("Google Speech Recognition could not understand audio")

    f.write(" ")

f.close()
