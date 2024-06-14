#libraries-----------------------------------------------------------------
import pyttsx3
import speech_recognition as sr
import time
#variables-----------------------------------------------------------------
r = sr.Recognizer()
keywords = [("baybrus",1),("hey baybrus",1)]
source = sr.Microphone()
#functions-----------------------------------------------------------------
# speaks-------------------------------------------------------------------
def Speak(text):
    rate = 100;
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    engine.setProperty('rate', rate+50)
    engine.say(text)
    engine.runAndWait()
# Callback function---------------------------------------------------------
def callback(recognizer,audio):
    try:
        speech_as_text = recognizer.recognizer_sphinx(audio, keyword_entries=keywords)
        print(speech_as_text)
        if "Baybrus" in speech_as_text or "hi baybrus" :
            Speak("hello sir ?")
            recognizer_main()
    except sr.UnknownValueError:
        print("Oops didn't catch up with you buddy !")
# start Recognizer-------------------------------------------------------------
def start_recognizer():
    print("Waiting you for buddy")
    r.listen_in_background(source,callback)
    time.sleep(1000000)
# Main function for speech recognition-----------------------------------------
def recognizer_main():
    with sr.Microphone() as source:
        print("Say Something")
        audio = r.listen(source)
        data = ""
        try:
            data = r.recognize_google(audio).lower()  # Correct method usage here
            print("You said: " + data)
            # Respond to different commands
            if "how are you" in data:
                Speak("I am fine")
            elif "hello" in data:
                Speak("What's up buddy")
            else:
                Speak("I am sorry sir")
        except sr.UnknownValueError:
            print("Baybrus did not understand your input")
        except sr.RequestError as e:
            print("Couldn't understand: {0}".format(e))
#mainprogram---------------------------------------------------------------
while 1:
    start_recognizer()
