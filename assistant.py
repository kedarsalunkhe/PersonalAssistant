import wikipedia
import pyttsx3
import datetime
import speech_recognition as sr
import webbrowser
import os
from playsound import playsound


engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 130)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishme():
    hour = int(datetime.datetime.now().hour)

    if hour >= 0 and hour < 12:
        speak("Good Morning!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon")

    else:
        speak("Good evening")

    speak("Hey Kedar I am your personal assistant JARVIS v2.0, please tell me How may i help you")


def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print("Say that again")
        return "None"
    return query


if __name__ == "__main__":

    wishme()
    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('searching wikipedia')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("according to wikipedia")
            speak(results)
        
        elif 'open youtube' in query:
            webbrowser.open("https://www.youtube.com/")

        elif 'open google' in query:
            webbrowser.open("https://www.google.com/")

        elif 'open twitter' in query:
            webbrowser.open("https://www.twitter.com/")

        elif 'the time' in query:
            strtime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"KD The time is {strtime}")

        elif 'open filmora' in query:
            path = "C:\\Program Files (x86)\\Wondershare\\Wondershare Filmora\\Wondershare Filmora X.exe"
            os.startfile(path)

        elif 'wish navratri' in query:
            speak("Happy navratri to all the ladies out there")

        elif 'open my mail' in query:
            webbrowser.open("https://mail.google.com/mail/u/0/#inbox")
        
        elif 'play hanuman chalisa' in query:
            speak("Jai Shri Ram")
            print("Playing Hanuman Chalisa")
            playsound('D:\\hanuman-chalisa.mp3')

        elif 'quit' in query:
            quit()
            


        

