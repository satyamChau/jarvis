#   from ast import main

from http import server
import sre_compile
from tkinter.tix import MAIN
from email.mime import audio
# from lib2to3.pytree import _Results
from unittest import result
import webbrowser
import pyttsx3
import datetime
import wikipedia
import speech_recognition as sr
import os
import smtplib

engine = pyttsx3.init('sapi5')
voice = engine.getProperty('voices')
# print(voice[1].id)
engine.setProperty('voice', voice[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon")

    else:
        speak("Good Evening")

    speak("I am Jarvis Sir. Please tell me how may I help you")


def takeCommand():

    # It takes microphone input from the user and return string as output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing......")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said:{query}\n")

    except Exception as e:
        # print(e)

        print("Say that again please.......")

        return "None"

    return query
def sendEmail(to, content):
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login('chauhansatyam0000@gmail.com', 'Satyamchauhan0@')
        server.sendmail('chauhansatyam0000@gmail.com', to, content)
        server.close()


if __name__ == "__main__":
    # speak("harry is a good boy")
    wishMe()

    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", "")

            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            speak(results)
            # print(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'open chrome' in query:
            webbrowser.open("chrome.com")     
        elif 'open whatsapp' in query:
            webbrowser.open("whatsapp.com")
        elif 'open facebook' in query:
            webbrowser.open("facebook.com")   
        elif 'open instagram' in query:
            webbrowser.open("instagram.com")     
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'open leetcode' in query:
            webbrowser.open("leetCode.com")
        elif 'open hackerrank' in query:
            webbrowser.open("hackerrank.com")
        elif 'play music' in query:
            music_dir = 'D:\\NOn critical sonf \\ songs\\favorite song'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f" Sir,The time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\Shobhit Chauhan\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'email to satyam' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "chauhansatyam0000@gmail.com"
                sendEmail(to, content)
                speak("Email  has been send")

            except Exception as e:
                print(e)
                speak("Sorry my friend satyam bhai . I am not able to send this email")
