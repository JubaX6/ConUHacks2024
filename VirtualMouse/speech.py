import speech_recognition as sr
import pyautogui
import pyaudio
from pynput.mouse import Controller, Button
import os
from pprint import pprint


class SpeechRecognition:

    def __init__(self):
        self.recognizer = sr.Recognizer()


    def recognize_speech(self):
        with sr.Microphone() as source:
            while True:
                print("Listening...")
                self.recognizer.adjust_for_ambient_noise(source, duration=1)
                audio = self.recognizer.listen(source)

                try:
                    text = self.recognizer.recognize_google(audio).lower()
                    print(f"You said: {text}")
                    self.identifying_command(text)
                except sr.UnknownValueError:
                    print("Sorry could not understand audio.")
                    return None
                except sr.RequestError as e:
                    print(f"Could not request results from Google Speech Recognition service; {e}")
                    return None


    def identifying_command(self, text):
        if text == "chrome":
            print("Opening Google Chrome")
            os.system("start chrome")
        elif text == "explorer":
            print("Opening explorer")
            os.system("Explorer ")
        elif text == "notepad":
            print("Opening Notepad")
            os.system("notepad")
        elif text == "calculator":
            print("Opening calculator")
            os.system(" calc ")
        elif text == "powerpoint":
            print("Opening PowerPoint")
            os.system("start powerpnt")
        elif text == "excel":
            print("Opening Excel")
            os.system("start excel")
        elif text == "word":
            print("Opening Microsoft Word")
            os.system("start winword")
        elif text == "code":
            print("Opening Visual Studio Code")
            os.system("code")
        elif text == "microsoft edge":
            print("Opening Microsoft Edge")
            os.system("start msedge")
        elif text == "command prompt":
            print("Opening command prompt")
            os.system("cmd")
        elif text == "exit":
            print("Exiting the program, goodbye!")
            exit(0)
        else:
            print("Command does not exist")

