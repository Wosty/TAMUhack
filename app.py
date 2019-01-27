from flask import Flask, request, render_template
from time import sleep
import sys, json, os, urllib
import requests
from urllib.request import Request, urlopen
from urllib.parse import urlencode


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/recieve', methods=['POST'])
def recieveImage():
    req = requests.get(['media'])
    with open('student.jpg', 'wb') as openFile:
        openFile.write(req.content)
    sleep(60)

    return "ok", 200
    

