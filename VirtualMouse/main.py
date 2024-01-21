import subprocess


def run_another_file(file_path):
    try:
        subprocess.run(["python", file_path], check=True)
        print(f"Successfully ran {file_path}")
    except subprocess.CalledProcessError as e:
        print(f"Error running {file_path}: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


def main():
    user_choice = int(input("Enter 1 to run the gesture detection, or enter 2 for the speech recognition:"))

    if user_choice != 1 and user_choice != 2:
        print("Error: Please enter 1 or 2.")
        return

    if user_choice == 1:
        run_another_file("virtual_mouse.py")
    if user_choice == 2:
        run_another_file("Grid_Voice_Overlay.py")


if __name__ == "__main__":
    main()
