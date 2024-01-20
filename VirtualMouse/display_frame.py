import cv2
import pyautogui


def display_frame(cap, screen_width, screen_height):
    while True:
        _, frame = cap.read()
        # Additional display logic if needed

        frame = cv2.flip(frame, 1)
        cv2.imshow('Virtual Mouse', frame)
        cv2.waitKey(1)
