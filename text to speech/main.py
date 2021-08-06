import pyttsx3
import os
# import Engine
engine = pyttsx3.init()
url = input("Enter the text to speak : -")
engine.say(url)
engine.runAndWait()