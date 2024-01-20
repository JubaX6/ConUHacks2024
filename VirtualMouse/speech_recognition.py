import speech_recognition as sr
import pyautogui
import pyaudio
from pynput.mouse import Controller, Button
import os


def recognize_speech():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        audio = recognizer.listen(source)

        try:
            text = recognizer.recognize_google(audio).lower()
            return text
        except sr.UnknownValueError:
            print("Sorry could not understand audio.")
            return None
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")
            return None


if __name__ == "__main__":
    while True:
        recognized_text = recognize_speech()
        if recognized_text:
            print("Recognized Text:", recognized_text)
        screen_width,  screen_height = pyautogui.size()
        middle_x = screen_width // 2
        middle_y = screen_height // 2

        mouse = Controller() #Mouse Controller
        mouse.position = (middle_x, middle_y)
        if recognized_text == "hello":
            print("performing right click")
            mouse.click(Button.right)
        if recognized_text == "chrome":
            print("Opening Google Chrome")
            os.system("start chrome")
        if recognized_text == "explorer":
            print("Opening explorer")
            os.system("Explorer ")
        if recognized_text == "notepad":
            print("Opening Notepad")
            os.system("notepad")
        if recognized_text == "calculator":
            print("Opening calculator")
            os.system(" calc ")
        if recognized_text == "powerpoint":
            print("Opening PowerPoint")
            os.system("start powerpnt")
        if recognized_text == "excel":
            print("Opening Excel")
            os.system("start excel")
        if recognized_text == "word":
            print("Opening Microsoft Word")
            os.system("start winword")
        if recognized_text == "code":
            print("Opening Visual Studio Code")
            os.system("code")
        if recognized_text == "microsoft edge":
            print("Opening Microsoft Edge")
            os.system("start msedge")
        if recognized_text == "command prompt":
            print("Opening command prompt")
            os.system("cmd")
        if recognized_text == "exit":
            print("Goodbye")
            exit(0)