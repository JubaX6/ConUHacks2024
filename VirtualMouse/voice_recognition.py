import speech_recognition as sr
import pyautogui


def voice_recognition(exit_event):
    recognizer = sr.Recognizer()

    while not exit_event.is_set():
        with sr.Microphone() as source:
            try:
                audio = recognizer.listen(
                    source, timeout=5, phrase_time_limit=2)
                command = recognizer.recognize_google(audio).lower()
                print(f"{command}")

                if "click" in command:
                    pyautogui.click()
                elif "exit" in command:
                    exit_event.set()  # Set the exit event to signal other threads to exit

            except sr.UnknownValueError:
                pass  # Handle the case where speech recognition could not understand the command
            except sr.RequestError as e:
                print(f"Speech recognition request failed: {e}")
