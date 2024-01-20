import cv2
import mediapipe as mp
import pyautogui
import math
import speech_recognition as sr
from speech_recognition import Recognizer

cap = cv2.VideoCapture(0)
hand_detector = mp.solutions.hands.Hands()
drawing_utils = mp.solutions.drawing_utils

# Screen resolution (adjust accordingly)
screen_width, screen_height = pyautogui.size()

# Threshold for triggering a click (adjust accordingly)
click_threshold = 30

# Snap distance for snapping onto clickable regions
snap_distance = 50

# List of clickable regions (x, y, width, height)
clickable_regions = [(100, 100, 50, 50),
                     (300, 200, 50, 50), (500, 300, 50, 50)]

# Initialize the speech recognition recognizer
recognizer = Recognizer()

while True:
    _, frame = cap.read()
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    output = hand_detector.process(rgb_frame)
    hands = output.multi_hand_landmarks

    first_index_finger = True  # Reset the flag for each iteration

    if hands:
        for hand in hands:
            # Track the first index finger
            index_finger_landmark = hand.landmark[8]
            thumb_landmark = hand.landmark[4]

            height, width, _ = frame.shape
            cx_index, cy_index = int(
                index_finger_landmark.x * width), int(index_finger_landmark.y * height)
            cx_thumb, cy_thumb = int(
                thumb_landmark.x * width), int(thumb_landmark.y * height)

            # Invert the mouse coordinates
            inverted_mouse_x = screen_width - cx_index
            # inverted_mouse_y = cy_index

            # Calculate the distance between thumb and index finger
            distance = math.sqrt((cx_thumb - cx_index) **
                                 2 + (cy_thumb - cy_index)**2)

            # Move the mouse cursor based on the inverted coordinates
            pyautogui.moveTo(inverted_mouse_x, cy_index)  # inverted_mouse_y)

            cv2.circle(frame, (cx_index, cy_index), 10, (0, 255, 0), -1)

            # Check if the distance is below the threshold for a click
            if distance < click_threshold:
                pyautogui.click()

                # Optional: Add a delay to avoid multiple rapid clicks
                # time.sleep(0.5)

            # # Check for snap-on to clickable regions
            # for region in clickable_regions:
            #     region_x, region_y, region_width, region_height = region
            #     if (
            #         region_x <= inverted_mouse_x <= region_x + region_width
            #         and region_y <= cy_index <= region_y + region_height
            #     ):
            #         # Cursor is within snap distance of the clickable region, snap on
            #         pyautogui.moveTo(region_x + region_width //
            #                          2, region_y + region_height // 2)

    # Recognize voice commands
    with sr.Microphone() as source:
        try:
            audio = recognizer.listen(source, timeout=5)
            command = recognizer.recognize_google(audio).lower()

            if "click" in command:
                pyautogui.click()

        except sr.UnknownValueError:
            pass  # Handle the case where speech recognition could not understand the command
        except sr.RequestError as e:
            print(f"Speech recognition request failed: {e}")

    frame = cv2.flip(frame, 1)
    cv2.imshow('Virtual Mouse', frame)
    cv2.waitKey(3)
