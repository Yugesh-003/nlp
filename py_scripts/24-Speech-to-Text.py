# !pip install SpeechRecognition

import speech_recognition as sr

audio_file = ("Sample.wav")
r = sr.Recognizer()   #  Creates a Recognizer object from the speech_recognition library.
# This object has methods for recognizing speech from audio

with sr.AudioFile(audio_file) as source:
    audio_data = r.record(source)   #  converts the raw sound into a format the recognizer can understand.
    # audio_data = r.record(source, duration=5)   # Fetch the part of first 5 seconds

    text = r.recognize_google(audio_data)
    # Sends the audio_data to Google’s free Web Speech API.
    # Returns the recognized speech as text.
    print(text)

