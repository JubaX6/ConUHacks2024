# ConUHacks2024

The NoKeyMouseis a project aimed at enhancing accessibility by introducing a virtual mouse that is controlled by a webcam or a voice command functionality for actions and screen navigation using a grid-based system. Leveraging the power of computer vision, the project utilizes OpenCV and MediaPipe for hand-tracking, enabling users to control the virtual mouse through hand gestures. Additionally, voice commands are supported through the integration of SpeechRecognition and PyAudio.

## Key Dependencies
- opencv-python
- mediapipe
- pyautogui
- speechrecognition
- pyaudio
- pynput

This project empowers users with diverse needs to interact with computers more effectively, making digital environments more inclusive and user-friendly.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [Acknowledgments](#acknowledgments)

## Acknowledgments

This project wouldn't have been possible without the incredible work of the following open-source libraries:

- [OpenCV-Python](https://github.com/opencv/opencv-python): A versatile computer vision library that played a key role in implementing hand-tracking for our virtual mouse.

- [MediaPipe](https://github.com/google/mediapipe): We utilized MediaPipe for its efficient and accurate hand-tracking capabilities, enhancing the precision of our virtual mouse control.

- [PyAutoGUI](https://github.com/asweigart/pyautogui): PyAutoGUI facilitated the automation of on-screen mouse movements and clicks, contributing to the overall functionality of our accessibility assistant.

- [SpeechRecognition](https://github.com/Uberi/speech_recognition): This library enabled seamless integration of voice commands, allowing users to interact with the virtual mouse using spoken instructions.

- [PyAudio](https://github.com/intxcc/pyaudio): PyAudio played a crucial role in capturing and processing audio input, making voice command recognition possible in our project.

- [pynput](https://github.com/moses-palmer/pynput): Pynput provided essential tools for controlling and monitoring input devices, enhancing the overall user experience of our virtual accessibility assistant.

## Commands

The script continuously listens for voice commands using the SpeechRecognition library.

The commands include:
- grid cell coordinates 
- left click 
- right click 
- hide/show: hiding or showing the grid 
- application launching: "Chrome", "explorer", and ext. 
- starting the virtual mouse
- and exiting the program

The grid coordinates allow the user to navigate the screen with voice. Coordinated with the letters of the alphabet and integers, the user calls the square to navigate the mouse to and apply the appropriate commands. 
