import sys
import speech_recognition as sr
from countryinfo import CountryInfo
import pyttsx3
import random
import pyjokes
from wordhoard import Definitions
from datetime import date
from datetime import datetime
from pyowm.owm import OWM

owm = OWM('a40af9073f9a2e66a65b7b42cc53012a')
mgr = owm.weather_manager()

engine = pyttsx3.init()
rate = engine.getProperty("rate")

query = 0

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def speak2(audio, var):
    engine.say(audio + var)
    engine.runAndWait()

def speak3(var, audio, var1):
    engine.say(var + audio + var1)
    engine.runAndWait()


def getCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening for command........")
        audio = r.listen(source)
        print('Recognizing.........')
        query = r.recognize_google(audio)
        return query

def processCommand(query):
    if 'exit' in query:
        print('See you later!')
        speak('See you later!')


    elif 'hello' in query:
        greeting = ["hai!", "hey!", "how do you do?", "sup!", "hello!", "hello there!", "hai, how can i help?", "what's up"]
        greet = greeting[random.randint(0,len(greeting)-1)]
        speak(greet)
        print(greet)
        
    elif 'name' in query:
        print('My name is vivyd')
        speak('my name is vivyd')

    elif 'how are you' in query:
        print("I'm doing well, thank's for asking")
        speak("i'm doing well, thank's for asking")

    elif 'what are your functions' in query:
        print("I can tell time, give meanings for words, tell country capitals, tell jokes, tell the date, etc")
        speak("i can tell time, give meanings for words, tell country capitals, tell jokes, tell the date, etc")

    elif 'joke' in query:
        joke = pyjokes.get_joke()
        print(joke)
        speak(joke)

    elif 'meaning' in query:
        print('what is the word you want to search?')
        speak('what is the word you want to search?')
        word = getCommand()
        #word = query

        definition = Definitions(word)
        definiton_results = definition.find_definitions()

        print(definiton_results)
        speak(definiton_results)

    elif 'weather' in query:
        print("which city's weather do you want to know?")
        speak("which city's weather do you want to know?")

        city = getCommand()
        print(city)

        observation = mgr.weather_at_place(city)  # the observation object is a box containing a weather object
        weather = observation.weather
        #weather.status           # short version of status (eg. 'Rain')
        weather_status = weather.detailed_status  # detailed version of status (eg. 'light rain')

        print(weather_status)
        speak(weather_status)

    elif 'date' in query:
        today = date.today()
        d2 = today.strftime("%B %d, %Y")

        print("Today's date is", d2)
        speak2("Today's date is", d2)

    elif 'time' in query:
        now = datetime.now()

        dt_string = now.strftime("%H:%M")
        print("The current time is", dt_string)
        speak2("The current time is", dt_string)

    elif 'capital' in query:
        print("Which country's capital do you want to know about?")
        speak("Which country's capital do you want to know about?")

        country = getCommand()
        print(country)

        country1 = CountryInfo(country)
        capital = country1.capital()

        print(capital, 'is the capital of ', country)
        speak3(capital, 'is the capital of ', country)

while True:
    try:
        query = getCommand().lower()
        processCommand(query)
    except: 
        print("Try again...")

    