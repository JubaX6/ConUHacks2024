import cv2
import mediapipe as mp
import pyautogui
from queue import Queue


def hand_tracking(cap, screen_width, frame_queue, exit_event):
    hand_detector = mp.solutions.hands.Hands()
    is_index_finger_tracked = False

    while not exit_event.is_set():
        _, frame = cap.read()
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        output = hand_detector.process(rgb_frame)
        hands = output.multi_hand_landmarks

        if hands:
            for hand in hands:
                # Track the index finger only if it's not already being tracked
                if not is_index_finger_tracked:
                    index_finger_landmark = hand.landmark[8]

                    height, width, _ = frame.shape
                    cx_index, cy_index = int(
                        index_finger_landmark.x * width), int(index_finger_landmark.y * height)

                    # Invert the mouse coordinates
                    inverted_mouse_x = screen_width - cx_index

                    # Move the mouse cursor based on the inverted coordinates
                    pyautogui.moveTo(inverted_mouse_x, cy_index)

                    cv2.circle(frame, (cx_index, cy_index),
                               10, (0, 255, 0), -1)

                    # Set the flag to indicate that the index finger is being tracked
                    is_index_finger_tracked = True
                else:
                    # Clear the flag if the hand is not detected or other fingers are detected
                    is_index_finger_tracked = False

                # Check if the distance is below the threshold for a click

        frame = cv2.flip(frame, 1)

        # Put the frame into the queue for the main thread
        frame_queue.put(frame)
