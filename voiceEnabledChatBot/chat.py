import openai
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia as wiki
import webbrowser
import os
import smtplib
import pyaudio
import sys
import mysql.connector as c

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print("User said:", query)
    except Exception as e:
        print(e)
        speak("say that again please")
        print("say that again please...")
        return None
    return query
    

openai.api_key=""
model_engine="text-davinci-003"

while 1:
 prompt = takeCommand()
 if(prompt=="quit"):
     break
 if(prompt==None):
     continue
 completion=openai.Completion.create(
    engine=model_engine,
    prompt=prompt,
    max_tokens=1024,
    n=1,
    stop=None,
    temperature=0.5,
 )

 response=completion.choices[0].text
 speak(response)
