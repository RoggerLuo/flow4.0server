# -*- coding: utf-8 -*-
import os
import sys
import numpy as np
import cv2
import pickle
import face_recognition

# IMAGE_SIZE = 64
IMAGE_SIZE = 20

size = 300
user_photo_path = './user_photo'
# 按照指定图像大小调整尺寸


def resize(frame):
    rate = size / frame.shape[0]
    small_frame = cv2.resize(frame, (0, 0), fx=rate, fy=rate)
    return small_frame


# 目的， x为300px的二进制 图库数据,   不不，没必要，最后都是128维，300px用在识别的时候 动态提取实时视频流的大小
# 每一个人的向量为平均值， 每个人一个name，一个encode
# 这里只要  遍历所有的人员文件夹
# 针对每一个文件夹，读取出里面所有的照片，转换成ndarray然后，求平均值
# 然后append到总数组里
# 遍历所有的人员文件夹
def preload():
    pkl_data = []
    for dir_name in os.listdir(user_photo_path):
        # 读取出里面所有的照片
        dir_path_path = os.path.abspath(os.path.join(user_photo_path, dir_name))
        if not os.path.isdir(dir_path_path): continue
        if len(os.listdir(dir_path_path)) == 0: continue #如果里面没有照片，则跳过
        
        print(dir_name)
        encodings_sum = np.zeros(128)
        encodings_count = 0
        for photo_name in os.listdir(dir_path_path):
            if not (photo_name.endswith('.jpg') or photo_name.endswith('.bmp') or photo_name.endswith('.png') or photo_name.endswith('.jpeg')): continue
            print('   '+photo_name)
            # 转换成ndarray
            image_array = face_recognition.load_image_file(
                os.path.join(dir_path_path, photo_name))
            if len(face_recognition.face_encodings(image_array)) > 0:
                encoding1 = face_recognition.face_encodings(image_array)[0]
                # 加起来
                encodings_sum += encoding1
                encodings_count += 1
        # 然后，求平均值
        if encodings_count == 0: continue #如果一张人脸都没有找到
        even_encoding = encodings_sum / encodings_count
        pkl_data.append({'encoding': even_encoding, 'name': dir_name})

    # 存到pkc里
    with open('./user_photos_lib.pkl', 'wb') as f:
        pickle.dump(pkl_data, f, True)

    return 'ok'

# print(preload())