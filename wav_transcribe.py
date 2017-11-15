import speech_recognition as sr

# obtain path to "english.wav" in the same folder as this script
from os import path
WAV_FILE = path.join(path.dirname(path.realpath(__file__)), "microphone-results.wav")

# use "english.wav" as the audio source
r = sr.Recognizer()
with sr.WavFile(WAV_FILE) as source:
    audio = r.record(source) # read the entire WAV file

# recognize speech using Google Speech Recognition
try:
    print("Google Speech Recognition thinks you said " + r.recognize_google(audio))
    file=open('microphone-results.txt','w')
    file.write(r.recognize_google(audio))
    file.close()
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))


