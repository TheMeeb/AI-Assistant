#libraries-----------------------------------------------------------------
import pyttsx3
import SpeechRecognition
import time
#functions-----------------------------------------------------------------
def Speak(text):
    rate = 100;
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    engine.setProperty('rate', rate+50)
    engine.say(text)
    engine.runAndWait()
#mainprogram---------------------------------------------------------------
Speak("HelloWorld")
Speak("Fuck You")
