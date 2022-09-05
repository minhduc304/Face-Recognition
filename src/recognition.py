import face_recognition
import os

class EncodeFaces:

    def __init__(self):
        self.faces_folder = "/Users/admin/Face-recognition/faces"
        self.dict_faces = {}
        self.dict_encoding_faces = {}
        
    def load_images(self):
        self.faces = os.listdir(self.faces_folder)
        # self.dict_faces = {}

        for image in self.faces:
            name = image.replace(".jpg", "")
            path_to_image = os.path.join(self.faces_folder, image)
            loaded_image = face_recognition.load_image_file(path_to_image)

            self.dict_faces = {
                name: loaded_image
            }
        
        
    def encode_faces(self):
        self.load_images()

        for name, image in self.dict_faces.items():
            encoding = face_recognition.face_encodings(image)[0]
        
            self.dict_encoding_faces = {
                name: encoding
            }

        return self.dict_encoding_faces

    


a = EncodeFaces()
#print(a.load_images())
print(a.encode_faces())

