#-*- coding: utf-8 -*-
# import random

import numpy as np
from keras.models import load_model
import cv2
import pickle
# import face_recognition

# import sys
# sys.path.append("..")
# from Photo import IMAGE_SIZE, Photo
# from Directory import Directory

# from Photo import Photo, IMAGE_SIZE


def get_repo():
    with open('./user_photos_lib.pkl', 'rb') as f:
        return pickle.load(f)

        
class Model:

    def __init__(self):
        self.model = None

    # MODEL_PATH = './model/me.face.model.h5'
    def load_model(self, file_path):
        self.model = load_model(file_path)

    def predict(self,encoding1,encoding2):
        # encoding2 = face_recognition.face_encodings(image2)[0]
        concateSample = encoding1 - encoding2 #np.concatenate((encoding1, encoding2))
        # print('concateSample.shape')
        # print(concateSample.shape)
        concateSample = concateSample.reshape((1,128))
        # print('concateSample.shape after reshape')
        # print(concateSample.shape)

        rs = self.model.predict(concateSample,1)
        return rs[0][1]


# def compare_face(encoding1,repo,model):
#     print('repo[0]shape')
#     print(repo[0]['encoding'])
#     print('encoding1')
#     print(encoding1.shape)
#     scores = [ model.predict(encoding1,item['encoding']) for item in repo]
#     ind = scores.index(max(scores))
#     # print(repo[ind]['name'])
#     return repo[ind]['name']

