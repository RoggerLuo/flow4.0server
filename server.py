#!/usr/bin/env python
from flask_cors import *
from flask import Flask, render_template, Response, request
import json
import mysql_operation as sql
from machine_learning.findSimilar import findWord

app = Flask(__name__, static_folder='static')
CORS(app, supports_credentials=True)

@app.route('/search/<word>', methods=['POST', 'GET'])
def search(word):
    if request.method == 'GET':
        found_list = findWord()
        
        if len(notes) != 0:
            return json.dumps(notes)
        else:
            return json.dumps([])


@app.route('/notes', methods=['POST', 'GET'])
def notes():
    if request.method == 'GET':
        notes = sql.readNotes()
        if len(notes) != 0:
            return json.dumps(notes)
        else:
            return json.dumps([])


@app.route('/note/<item_id>', methods=['POST', 'GET'])
def note(item_id):
    if request.method == 'GET':
        notes = sql.readNotesById(item_id)
        if len(notes) != 0:
            return json.dumps(notes[0])
        else:
            return json.dumps({})

    if request.method == 'POST':
        request.form['content']

    return json.dumps('not found')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5555)  # ,  debug=True
