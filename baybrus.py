#libraries-----------------------------------------------------------------
import pyttsx3
import speech_recognition as sr
import time
import random 
from openpyxl import load_workbook 
#variables-----------------------------------------------------------------
r = sr.Recognizer()
keywords = [("baybrus",1),("hey baybrus",1)]
source = sr.Microphone()
#functions-----------------------------------------------------------------
# speaks-------------------------------------------------------------------
def Speak(text):
    rate = 100
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
            data = r.recognize_google(audio).lower()  # Correct method usage here--------------
            print("You said: " + data)
            # Respond to different commands-------------------------------------
            if data in hello_list:
                Speak(random.choice(reply_hello))
                time.sleep(2)
            elif data in how_are_you:
                Speak(random.choice(reply_hello_are_you))
                time.sleep(2)
            else:
                Speak("I am sorry sir")
        except sr.UnknownValueError:
            print("Baybrus did not understand your input")
        except sr.RequestError as e:
            print("Couldn't understand: {0}".format(e))
# Excel response function ------------------------------------------------------
def excel():
    # Load the workbook
    wb = load_workbook("/home/meeb/project/file.xlsx")
    
    # Accessing 'User' worksheet
    wu = wb['User']
    
    # Accessing 'Replies' worksheet
    wr = wb['Replies']
    
    # Initialize lists
    global hello_list, how_are_you, reply_hello_list, reply_how_are_you
    
    # Extracting values from rows in 'User' worksheet
    hello_list = [cell.value for cell in wu['1']]
    how_are_you = [cell.value for cell in wu['2']]
    
    # Extracting values from rows in 'Replies' worksheet
    reply_hello_list = [cell.value for cell in wr['1']]
    reply_how_are_you = [cell.value for cell in wr['2']]
#mainprogram---------------------------------------------------------------
excel()
while 1:
    start_recognizer()
