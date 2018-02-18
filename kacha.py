import cv2
import face_recognition
import time
import json

color = (0, 255, 0)
size = 128
face_margin = 15

classfier = cv2.CascadeClassifier(
    "/Users/RogersMac/opcv/opencv-3.0.0/data/haarcascades/haarcascade_frontalface_alt.xml")


def compare_face(encoding1, repo, model):
    scores = [model.predict(encoding1, item['encoding']) for item in repo]
    ind = scores.index(max(scores))
    print(max(scores))
    return repo[ind]['name'], scores[ind]


class KachaCamera(object):

    def __init__(self):
        self.video = cv2.VideoCapture(0)

    def resize(self, frame):
        if frame.shape[0] != 0:
            rate = size / frame.shape[0]
            frame = cv2.resize(frame, (0, 0), fx=rate, fy=rate)

        return frame

    def rectangle(self, frame):
        # frame = self.resize(frame)
        greyFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faceRects = classfier.detectMultiScale(
            greyFrame, scaleFactor=1.2, minNeighbors=3, minSize=(32, 32))

        if len(faceRects) > 0:
            return faceRects[0]
        else:
            return []

    def kacha(self,name):
        success, image = self.video.read()
        cv2.imwrite(  './user_photo/'+name+'/'+str(int(10*time.time()))+'.jpg', image) 
        return    json.dumps('ok')                            

    def do_something_with_image(self, faceLocation, image):
        x, y, w, h = faceLocation
        image = image[y - 60: y + h + 60, x - 60: x + w + 60]
        image = self.resize(image)

        face_encodings = face_recognition.face_encodings(image)
        if len(face_encodings) >= 1:
            face_encoding = face_encodings[0]
            rs, perc = compare_face(face_encoding, self.repo, self.model)
            print("识别结果:【%s】" % (rs))
            print("识别所用时间%f秒" % (time.time() - self.last_time))
            # print(perc)

    def __del__(self):
        self.video.release()
