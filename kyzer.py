import speech_recognition as sr                       
import pyttsx3
#import pywhatkit
import datetime
import os
import pyjokes

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
username = ""

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    engine.setProperty("rate",145)

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >=0 and hour<12:
        speak("Good Morning Boss!")
    elif hour >=12 and hour<18:
        speak("Good Afternoon Boss!")
    else:
        speak("Good Evening Boss!")

    speak("Kyzer is activated . Please tell me how may I help you!")

def takeCommand():
    # It takes microphone input from the user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source,timeout=3, phrase_time_limit=3)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language= 'en-in')

    except Exception as e:
        print(e)
        engine.setProperty("rate", 120)
        print("Say that again, please.....")
        speak("Say that again, please")
        return "None"
    return query


if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        if 'play' in query:
           song = query.replace('play','')
           speak('playing '+ song)
 #          pywhatkit.playonyt(song)
        elif 'time'in query:
           time = datetime.datetime.now().strftime('%I:%M 5p')
           speak('Current time is ' + time)
        elif 'who the heck is ' in query:
           person = query.replace('who the heck is', '')
        
        elif 'date' in query:
           print(query) 
           speak('sorry,I have a headache i will not tell you') 
        elif 'are you single' in query:
           print(query)
           speak('I am in relationship with wifi')
        elif 'hello' in query:
           print(query)
           speak('Hii sir')
        elif 'how are you' in query:
           print(query)
           speak('I am fine sir')
        elif 'kyzer any updates ' in query:
           print(query)
           speak('i am checking sir')
        elif 'i am waiting  kyzer' in query:
           print(query) 
           speak('Work is in progress')
        elif 'spotify' in query:
           os.startfile('%USERDIR%') #Add app directory here
        elif 'joke' in query:
           speak(pyjokes.get_joke())


