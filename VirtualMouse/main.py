import cv2
import mediapipe as mp
import pyautogui

cap = cv2.VideoCapture(0)
hand_detector = mp.solutions.hands.Hands()
drawing_utils = mp.solutions.drawing_utils

# Screen resolution (adjust accordingly)
screen_width, screen_height = pyautogui.size()

while True:
    _, frame = cap.read()
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    output = hand_detector.process(rgb_frame)
    hands = output.multi_hand_landmarks

    first_index_finger = True  # Reset the flag for each iteration

    if hands:
        for hand in hands:
            # Only track the first index finger
            if first_index_finger:
                index_finger_landmark = hand.landmark[8]
                height, width, _ = frame.shape
                cx, cy = int(index_finger_landmark.x *
                             width), int(index_finger_landmark.y * height)

                # Invert the mouse coordinates
                inverted_mouse_x = screen_width - cx
                # inverted_mouse_y = cy

                # Move the mouse cursor based on the inverted coordinates
                pyautogui.moveTo(inverted_mouse_x, cy)  # inverted_mouse_y)

                cv2.circle(frame, (cx, cy), 10, (0, 255, 0), -1)

                # Set the flag to False to stop tracking additional index fingers
                first_index_finger = False

    frame = cv2.flip(frame, 1)
    cv2.imshow('Virtual Mouse', frame)
    cv2.waitKey(1)
