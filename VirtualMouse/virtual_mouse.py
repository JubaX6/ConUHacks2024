import cv2
import threading
import hand_tracking
import voice_recognition
import display_frame
import pyautogui
from queue import Queue

def main():
    # Shared variables
    screen_width, screen_height = pyautogui.size()

    # Shared variables for hand tracking
    cap = cv2.VideoCapture(0)
    frame_queue = Queue()
    exit_event = threading.Event()

    # Create and start threads
    hand_thread = threading.Thread(
        target=hand_tracking.hand_tracking, args=(cap, screen_width, frame_queue, exit_event))
    voice_thread = threading.Thread(target=voice_recognition.voice_recognition, args=(exit_event,))

    # Start threads
    hand_thread.start()
    voice_thread.start()

    while not exit_event.is_set():
        if not frame_queue.empty():
            frame = frame_queue.get()

            # Display the frame in the main thread
            cv2.imshow('Virtual Mouse', frame)
            cv2.waitKey(1)

    # Release camera resource
    cap.release()

    # Wait for threads to finish before exiting
    hand_thread.join()
    voice_thread.join()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
