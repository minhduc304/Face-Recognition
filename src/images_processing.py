import cv2
import tkinter
from PIL import Image, ImageTk
import datetime
import os
from imutils.video import VideoStream
import imutils
import time
import numpy as np


class App():
    
    def __init__(self, window, window_title, video_source=0):
        self.window = window
        self.window.title = window_title

        self.video_source = video_source

        self.vid = MyVideoCapture(video_source)    
        self.canvas = tkinter.Canvas(window, width = self.vid.width, height = self.vid.height)
        self.canvas.pack()

        self.btn_capture=tkinter.Button(window, text="Capture", width=50, command=self.capture)
        self.btn_capture.pack(anchor=tkinter.CENTER, expand=True)
        self.delay = 1
        self.update()

        self.window.mainloop()

    def capture(self):
        timestamp = datetime.datetime.now()
        filename = "{}.jpg".format("frame" + timestamp.strftime("%d/%m/%Y_%H-%/M-%S"))
        path = os.path.join("/Users/admin/Face-recognition/snapshots", filename)

        ret, frame = self.vid.get_frame()

        if ret:
            cv2.imwrite(path, cv2.cvtColor(frame, cv2.COLOR_RGB2BGR))
            return "Save successful."


    def update(self):
        ret, frame = self.vid.get_frame()
        if ret:
            self.photo = ImageTk.PhotoImage(image = Image.fromarray(frame))
            self.canvas.create_image(0, 0, image = self.photo, anchor = tkinter.NW)
        self.window.after(self.delay, self.update)

    

class MyVideoCapture():

    def __init__(self, video_source):
        self.vid = cv2.VideoCapture(video_source)
        if not self.vid.isOpened():
            raise ValueError("Unable to open video source",video_source)
        self.width = self.vid.get(cv2.CAP_PROP_FRAME_WIDTH)
        self.height = self.vid.get(cv2.CAP_PROP_FRAME_HEIGHT)
    

    def get_frame(self):
        if self.vid.isOpened():
            ret, frame = self.vid.read()
            frame = cv2.resize(frame,(640,480))
            if ret:
                return (ret, cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
            else:
                return (ret,None)

    def __del__(self):
        if self.vid.isOpened():
           self.vid.release()
    

    
    

App(tkinter.Tk(), "Tkinter and OpenCV")

