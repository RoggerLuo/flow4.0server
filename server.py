from flask_cors import *
from flask import Flask, render_template, Response, request
import json
import mysql_operation as sql
from w2v.findSimilar import findWord

app = Flask(__name__, static_folder='static')
CORS(app, supports_credentials=True)


@app.route('/search/<word>', methods=['GET'])
def search(word):
    found_list = findWord(word, 20)
    if len(found_list) != 0:
        return json.dumps(found_list)
    else:
        return json.dumps([])


@app.route('/notes', methods=['GET'])
def notes():
    notes = sql.readNotes()
    if len(notes) != 0:
        return json.dumps(notes)
    else:
        return json.dumps([])


@app.route('/note/<item_id>', methods=['POST', 'PUT', 'DELETE'])
def note(item_id):
    if (request.method == 'POST') or (request.method == 'PUT'):
        content = request.form['content']
        sql.touchNote(item_id, content)
    
    if request.method == 'DELETE':
        sql.deleteNote(item_id)
    
    return json.dumps('ok')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5555)  # ,  debug=True


# if request.method == 'GET':
#     notes = sql.readNotesById(item_id)
#     if len(notes) != 0:
#         return json.dumps(notes[0])
#     else:
#         return json.dumps({})
