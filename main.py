import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import smtplib
from moviepy.editor import *
import pygame
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def maen():
    hr = int(datetime.datetime.now().hour)
    if hr>=0 and hr<12:
        speak("Good Morning")
    elif hr>=12 and hr<=18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")
    speak("I am your assistant Zira ,Please tell me how may i help you")

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source)

    try:
        print("Recognising...")
        query = r.recognize_google(audio,language='en-in')
        print(f"user said : {query}\n")
    except Exception as e:
        print("Something went wrong.Try again..")
    return query

def sendemail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('lprr1003@gmail.com','ethrtjrqsbjgwhsm')
    server.sendmail('lprr1003@gmail.com',to,content)
    server.close()

if __name__ == '__main__':
    maen()
    while(True):
        query = listen().lower()
        if 'wikipedia' in query:
            speak("Searching wikipedia")
            query = query.replace('wikipedia','')
            results = wikipedia.summary(query,sentences=2)
            speak("According to wikipedia")
            speak(results)

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'play songs' or 'play music' in query:
            m_dir = "D:\\parul phone\\music"
            songs = os.listdir(m_dir)
            os.startfile(os.path.join(m_dir,songs[0]))

        elif 'the time' in query:
            strtime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is {strtime}")

        elif 'open pycharm' in query:
            code_path = "D:\\newPycharm\\PyCharm Community Edition 2021.2.2\\bin\\pycharm64.exe"
            os.startfile(code_path)

        elif 'open whatsapp' in query:
            path = "https://web.whatsapp.com//"
            os.startfile(path)

        elif 'send mail' in query:
            try:
                speak("Tell me the content of mail")
                content = listen()
                speak("Tell me the email id to whom you want to send the mail")
                to = listen()
                to = to.replace(' ','')+'@gmail.com'
                sendemail(to,content)
                speak("Email has been sent")

            except Exception as e:
                print(e)
                speak("Something went wrong")

        elif 'play video' in query:
            clip = VideoFileClip('D:\\kaam ki cheej\\wedding.mp4').resize(0.5)
            clip.preview()
            pygame.quit()

        elif 'shut down' in query:
            os.system("shutdown /s /t 1")

        elif 'open notepad' in query:
            os.system("C:\\Windows\\notepad.exe")









