# -*- coding: utf-8 -*-


import pyttsx3
engine = pyttsx3.init()
engine.setProperty('rate', 150) 

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

engine.say("I will speak this text")
engine.runAndWait() 




