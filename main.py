import speech_recognition as sr
import pyttsx3 
import pywhatkit
import datetime 
import wikipedia
import pyjokes
import calendar
from datetime import date 

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):  
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print("Listening..")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alex' in command:
                command = command.replace('alex', '')
                talk(command) 
    except:
        pass
    return command


def run_alexa():
    takecom = take_command()
    print(takecom)
    if 'play' in takecom:
        song = takecom.replace('play', '')
        talk('Playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in takecom:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('The current time is' + time)
    elif 'who is' in takecom:
        person = takecom.replace('who is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'what is' in takecom:
        item = takecom.replace('what is', '')
        info = wikipedia.summary(item, 1)
        print(info)
        talk(info)
    elif 'Activate self-destruct' in takecom:
        talk('3, 2, 1, Boom!')   
    elif 'joke' in takecom:
       talk(pyjokes.get_joke())
    elif  'day' in takecom:
      d = date.today()
      print('The date is:', d)
      t = calendar.day_name[d.weekday()]
      print('The day is', t)
      talk('The day is' + t)
    elif 'stop' in takecom:
        run_alexa = False
    else:
        talk('Please say that again.')

    run_alexa()
