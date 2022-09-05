import cv2
from tkinter import Tk, Label, Button
from PIL import Image, ImageTk
import datetime
import os
from imutils.video import VideoStream
import imutils
import time
import face_recognition
import recognition
import numpy as np


class FaceRecognitionApp():
    
    def __init__(self, stream):
        self.window = Tk()
        self.panel = None
        self.videostream = stream
        self.frame = None
        self.stop = False
        

        btn = Button(self.window, text="Snapshot!",
			command=self.capture)    
        btn.pack(side="bottom", fill="both", expand="yes", padx=10,
			pady=10)

        self.window.wm_protocol("WM_DELETE_WINDOW", self.close)

    def video_loop(self):
        while self.stop == False:

            self.frame = self.videostream.read()
            self.frame = imutils.resize(self.frame, width=300)
            self.label = Label(self.window)

            image = cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGB)
            image = Image.fromarray(image)
            imgtk = ImageTk.PhotoImage(image)

            self.label.imgtk = imgtk
            self.label.configure(image=imgtk)
            


    def capture(self):
        timestamp = datetime.datetime.now()
        filename = "{}.jpg".format(timestamp.strftime("%d/%m/%Y_%H-%/M-%S"))
        path = os.path.join("/Users/admin/Face-recognition/snapshots", filename)

        if self.frame is None:
            return "Frame is none."
        else:
            cv2.imwrite(path, self.frame.copy)
            return "Save successful."

        
    def close(self):
        self.stop = True
        self.videostream.stop()
        self.window.quit()


		
vs = VideoStream(src=0).start
time.sleep(2.0)

a = FaceRecognitionApp(vs)
a.window.mainloop()

