from camera import Camera
from model_and_repo import get_repo, Model
import threading


def recog():
    model = Model()
    print('模型初始化')
    model.load_model(file_path='./model/me.face.model.h5')
    print('人脸识别模型加载完毕')
    repo = get_repo()
    print('人脸库加载完毕')
    cam = Camera(model, repo)
    print('camera准备好了')
    while True:
        cam.get_frame()


def run():
    t = threading.Thread(target=recog, name='recognitionThread')
    t.start()
    t.join()


if __name__ == '__main__':
    recog()
