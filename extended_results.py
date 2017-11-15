#!/usr/bin/env python3

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
    # for testing purposes, we're just using the default API key
    # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY", show_all=True)`
    # instead of `r.recognize_google(audio, show_all=True)`
    from pprint import pprint
    print("Google Speech Recognition results:")
    pprint(r.recognize_google(audio, show_all=True)) # pretty-print the recognition result
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))
