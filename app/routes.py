#!/usr/bin/python3
from app import app
from flask import request, redirect, url_for, send_file
from flask_cors import CORS, cross_origin
import pyttsx3

CORS(app)

@app.route('/')
@app.route('/index')
@cross_origin(origin='*')
def index():
    #print("hey")
    return "TTS starting"

@app.route('/login', methods = ['POST', 'GET'])

def login():
    if request.method == 'POST':
        message = request.form['myField']
        print("Message : " + message)
        #print(message)
        return redirect(url_for('success',msg = message))
    else:
        message = request.args.get('myField')
        #print("Message : ")
        #print(message)
        return redirect(url_for('success',msg = message))


def text_to_speech(text, gender):

    voice_dict = {'Male': 0, 'Female': 1}
    code = voice_dict[gender]

    engine = pyttsx3.init()

    # Setting up voice rate
    engine.setProperty('rate', 155)

    # Setting up volume level  between 0 and 1
    engine.setProperty('volume', 1)

    # Change voices: 0 for male and 1 for female
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[code].id)

    #engine.save_to_file(text, './MyTTS/audio.mp3')
    engine.save_to_file(text, './audio.mp3')

    #engine.say(text)
    engine.runAndWait()

@app.route('/success/<msg>')
def success(msg):
    gender='Female'
    text_to_speech(msg, gender)
    
    return send_file("../audio.mp3", mimetype="audio/mp3")

