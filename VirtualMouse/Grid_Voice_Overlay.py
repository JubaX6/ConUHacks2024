import pyautogui
import speech_recognition as sr
import threading
import subprocess
import sys
import tkinter as tk
import virtual_mouse as vm

# Initialize Tkinter
root = tk.Tk()

# Set window transparency
root.wm_attributes("-transparentcolor", "gray")
root.config(bg='gray')

# Remove window borders and close button
root.overrideredirect(True)

# Set up grid parameters
grid_color = "white"  # White
grid_size = 20

# Get screen dimensions
screen_width, screen_height = pyautogui.size()

# Calculate grid size based on the minimum dimension of the screen
grid_size = min(screen_width, screen_height) // 20  # You can adjust this factor

# Flag to control whether the program should continue running
running = True

# Create a transparent canvas
canvas = tk.Canvas(root, width=screen_width, height=screen_height, bg='gray', highlightthickness=0)
canvas.pack()

# Draw the semi-transparent grid and labels
for x in range(0, screen_width, grid_size):
    for y in range(0, screen_height, grid_size):
        canvas.create_rectangle(x, y, x + grid_size, y + grid_size, outline=grid_color)

        # Calculate the position for the letter in the center of the cell
        letter_x = x + grid_size // 2
        letter_y = y + grid_size // 2

        # Get the corresponding letter for the row and number for the column
        row_letter = chr(ord('a') + y // grid_size)
        column_number = str(x // grid_size + 1)

        # Render the letter and number
        canvas.create_text(letter_x, letter_y, text=row_letter + column_number, fill=grid_color)


# Function to perform a click at the specified grid cell
def click_grid_cell(event):
    # Calculate the corresponding grid cell
    grid_column = event.x // grid_size
    grid_row = event.y // grid_size

    print(f"Clicked on cell: {chr(ord('a') + grid_row)}{grid_column + 1}")
    move_mouse_to_cell(grid_row, grid_column)


# Bind click event to the grid
root.bind("<Button-1>", click_grid_cell)


# Function to handle the window close event
def on_closing():
    global running, voice_thread
    running = False

    # Signal the voice_thread to exit gracefully
    if threading.current_thread() != voice_thread:
        voice_thread.join(timeout=1)

    # Cleanup or finalize tasks before exiting
    print("Exiting Tkinter main loop")
    root.destroy()


# Bind the window close event to the on_closing function
root.protocol("WM_DELETE_WINDOW", on_closing)

# Set the window to be always on top
root.attributes("-topmost", True)

# Initialize the recognizer
recognizer = sr.Recognizer()


# Function to move the mouse to the specified grid cell
def move_mouse_to_cell(grid_row, grid_column):
    # Calculate the coordinates of the center of the grid cell
    cell_center_x = grid_column * grid_size + grid_size // 2
    cell_center_y = grid_row * grid_size + grid_size // 2

    # Move the mouse to the cell
    pyautogui.moveTo(cell_center_x, cell_center_y, duration=0.25)


# Function to perform right click using PyAutoGUI (scheduled in the main thread)
def perform_right_click():
    pyautogui.click(button='right')


# Function to minimize the window
def hide_window():
    root.withdraw()  # Withdraw (hide) the window


# Function to show the window
def show_window():
    root.deiconify()  # Deiconify (show) the window


# Function to continuously listen for voice commands
def listen_for_commands():
    mouse_active = False
    exit_event = threading.Event()
    while running:
        with sr.Microphone() as source:
            try:
                print("Listening for commands...")
                audio = recognizer.listen(source, timeout=5, phrase_time_limit=2)
                command = recognizer.recognize_google(audio).lower()
                normalized_command = command.replace(" ", "")  # Remove spaces in the command

                print(f"Recognized command: {normalized_command}")

                # Normalize coordinates by removing any hyphens
                normalized_coordinates = normalized_command.replace("-", "")

                for grid_row in range(ord('a') - ord('a'), screen_height // grid_size):
                    for grid_column in range(screen_width // grid_size):
                        cell_name = f"{chr(ord('a') + grid_row)}{grid_column + 1}"
                        if cell_name == normalized_coordinates:
                            move_mouse_to_cell(grid_row, grid_column)
                            break

                if "leftclick" in normalized_command:
                    pyautogui.click()

                if "rightclick" in normalized_command:
                    # Execute right click in the main thread
                    root.after(0, perform_right_click)

                if "hide" in normalized_command:
                    root.after(0, hide_window)  # Schedule the hide_window function in the main thread

                if "show" in normalized_command:
                    root.after(0, show_window)  # Schedule the show_window function in the main thread

                if "exit" in normalized_command:
                    on_closing()

                if "pointer on" in normalized_command:
                    mouse_active = True
                    vm.main(exit_event)

                if "pointer off" in normalized_command:
                    mouse_active = False
                    vm.Pointer_Off(exit_event)

            except sr.UnknownValueError:
                print("Speech not detected")
            except sr.RequestError as e:
                print(f"Error connecting to Google API: {e}")


# Start listening for voice commands in a separate thread
voice_thread = threading.Thread(target=listen_for_commands)
voice_thread.start()

# Start Tkinter main loop
root.mainloop()

