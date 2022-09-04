import PIL
from PIL import Image,ImageTk
import cv2
from tkinter import *

from test import capture_image


width, height = 800, 600
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

window = Tk()
window.bind('<Escape>', lambda e: window.quit())
label_ = Label(window)
label_.pack()

def capture_image():
    return None

btn = Button(window, text="Snapshot!",
			command=capture_image)
btn.pack(side="bottom", fill="both", expand="yes", padx=10,
			pady=10)

def show_frame():
    _, frame = cap.read()
    frame = cv2.flip(frame, 1)
    cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
    img = PIL.Image.fromarray(cv2image)
    imgtk = ImageTk.PhotoImage(image=img)
    label_.imgtk = imgtk
    label_.configure(image=imgtk)
    label_.after(10, show_frame)
    



show_frame()
window.mainloop()
