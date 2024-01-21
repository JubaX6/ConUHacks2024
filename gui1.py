import customtkinter
import tkinterDnD
from PIL import Image 
    
IMAGE_PATH = r"C:\Users\atais\OneDrive\Desktop\download.jpg"
IMAGE_PATH2 = r"C:\Users\atais\OneDrive\Desktop\images.jpg"
IMAGE_PATH3 = r"C:\Users\atais\OneDrive\Desktop\Gesture-Recognition-and-Its-Application-in-Machine-Learning.jpg"
IMAGE_PATH4 = r"C:\Users\atais\OneDrive\Desktop\images.png"

customtkinter.set_ctk_parent_class(tkinterDnD.Tk)
customtkinter.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"

app = customtkinter.CTk(fg_color= "#007FFF")

screenwidth = app.winfo_screenwidth()
screenheight = app.winfo_screenheight()

app.geometry(f"{screenwidth}x{screenheight}")
app.title("NoKeyMouse")

def button_callback1():
    
    print()
    
def button_callback2():
    
    print()

your_image3 = customtkinter.CTkImage(light_image=Image.open(IMAGE_PATH3), size=(screenwidth/6 , screenheight/6))
label = customtkinter.CTkLabel(master=app, image=your_image3, text='')
label.pack(pady=20, padx=60, side = "left")

your_image4 = customtkinter.CTkImage(light_image=Image.open(IMAGE_PATH4), size=(screenwidth/6 , screenheight/6))
label = customtkinter.CTkLabel(master=app, image=your_image4, text='')
label.pack(pady=20, padx=60, side = "right")

your_image = customtkinter.CTkImage(light_image=Image.open(IMAGE_PATH), size=(screenwidth/6 , screenheight/6))
label = customtkinter.CTkLabel(master=app, image=your_image, text='')
label.pack(pady=20, padx=60)

frame_1 = customtkinter.CTkFrame(master=app,width = screenwidth/2, height= screenheight)
frame_1.pack(pady=60, padx=60, fill="both")

your_image2 = customtkinter.CTkImage(light_image=Image.open(IMAGE_PATH2), size=(screenwidth/6 , screenheight/6))
label = customtkinter.CTkLabel(master=app, image=your_image2, text='')
label.pack(pady=20, padx=60)

label_1 = customtkinter.CTkLabel(master=frame_1, justify=customtkinter.LEFT, text = "NoKeyMouse", font=("Arial", 25))
label_1.pack(pady=10, padx=10)

text_label = customtkinter.CTkLabel(master =frame_1, text="This program aims at assisting handicaped people in using a computer", font=("Arial", 15) )
text_label.pack(pady=10, padx=10)

button_1 = customtkinter.CTkButton(master=frame_1, command=button_callback1, text = "voice")
button_1.pack(pady=10, padx=10)

button_2 = customtkinter.CTkButton(master=frame_1, command=button_callback2, text = "gesture")
button_2.pack(pady=10, padx=10)
app.mainloop()
