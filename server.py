#!/usr/bin/env python
from flask_cors import *
from flask import Flask, render_template, Response
import json
import os

app = Flask(__name__, static_folder='user_photo')
CORS(app, supports_credentials=True)



# 一个notes
@app.route('/recognition')
def video_feed():
    while True:
        recog_cam.get_frame()


@app.route('/login', methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        if valid_login(request.form['username'],
                       request.form['password']):
            return log_the_user_in(request.form['username'])
        else:
            error = 'Invalid username/password'
    # the code below is executed if the request method
    # was GET or the credentials were invalid
    return render_template('login.html', error=error)



userFolder = './user_photo/'


model = Model()
print('模型初始化')
model.load_model(file_path='./model/me.face.model.h5')
print('人脸识别模型加载完毕')
repo = get_repo()
print('人脸库加载完毕')
recog_cam = Camera(model, repo)
recog_cam.get_frame()
# ------------ face recog -------------

@app.route('/recognition')
def video_feed():
    while True:
        recog_cam.get_frame()

    # os.popen('python3 recog.py')
    return 'ok'
    # recog.run()

    # m,r = getModel()
    # cam = Camera(m,r)
    # # gen(cam)
    # return Response(gen(cam),mimetype='multipart/x-mixed-replace;
    # boundary=frame')


@app.route('/preloadphoto')
def preloadphoto():
    preload()
    return json.dumps('ok')


# ------------ people -------------


@app.route('/allpeople')
def getPeople():
    return json.dumps(os.listdir(userFolder))


@app.route('/addperson/<name>')
def addPerson(name):
    if not os.path.exists(userFolder + name):
        os.mkdir(userFolder + name)
    return json.dumps('ok')


# ------------ photo -------------


@app.route('/photodelete/<name>/<filename>')
def photoDelete(name, filename):
    path = os.path.join(userFolder, name, filename)
    if os.path.exists(path):
        os.remove(path)
        return json.dumps('ok')
    return json.dumps('not found')


@app.route('/somebodysphoto/<name>')
def getPhotoList(name):
    if not os.path.exists(userFolder + name):
        return json.dumps([])
    return json.dumps(os.listdir(userFolder + name))


@app.route('/kacha/<name>')
def kacha(name):
    return cam.kacha(name)


# run
if __name__ == '__main__':
    app.run(host='0.0.0.0') #,  debug=True
