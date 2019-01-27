from flask import Flask, request, render_template
from time import sleep
import sys, json, os, urllib
import requests
import AzureCognitive_py.FaceAPI_locate_people_and_describe as fr
from urllib.request import Request, urlopen
from urllib.parse import urlencode
from picamera import picamera
import numpy as np

url = "https://tamuhack-face.herokuapp.com"
camera = PiCamera()
camera.rotation = 180
camera.start_preview()
sleep(1)
camera.capture('student.jpg')
files = {'media': open('student.jpg', 'rb')}
person = requests.post(url, files=files)
sleep(5)
camera.stop_preview()

f = open('Attendance.csv', 'w')

imageUrl = "https://tamuhack-face.herokuapp.com/student.jpg"
keyVal = "e7543f37a1494ac3badb987cd32cdc3d"
#landURL = "https://i.groupme.com/800x800.jpeg.bef3d27f7eed40229eeb6fe5b1eff15a.large"
#gabiURL = "https://i.groupme.com/640x640.jpeg.ff213177686c41f1ac2998e46402f919.large"
#wesURL = "https://i.groupme.com/1024x1024.jpeg.422a39028dbc492cab4d5280678643f1.large"
 
temp = ''
f.write('Student Name,Student ID')

fr.recogn(keyVal, imageUrl)

if (temp == 'Landon Creel'):
    f.write('Landon Creel,123\n')

if (temp == 'Wesley Till'):
    f.write('Wesley Till,234\n')

if (temp == 'Gabi Norsworthy'):
    f.write('Gabrielle Norsworthy,345\n')