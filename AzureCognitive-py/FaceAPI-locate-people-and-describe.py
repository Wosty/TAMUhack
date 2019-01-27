import http.client, urllib.request, urllib.parse, urllib.error, base64, requests, json, sys, json
import cognitive_face as CF
import requests
from io import BytesIO
from PIL import Image, ImageDraw

import http.client, urllib.request, urllib.parse, urllib.error, base64

keyVal = "6ab63c83e9914a1794de742dccc30330"
gabiURL = "https://i.groupme.com/640x640.jpeg.ff213177686c41f1ac2998e46402f919.large"
wesURL = "https://i.groupme.com/1024x1024.jpeg.422a39028dbc492cab4d5280678643f1.large"
landonURL = "https://i.groupme.com/800x800.jpeg.bef3d27f7eed40229eeb6fe5b1eff15a.large"

def is_male(attr):
    if attr == 'male':
        return True


def paraMade(key, url):
    subscription_key = key
    uri_base = 'https://centralus.api.cognitive.microsoft.com'
    headers = {
        'Content-Type': 'application/json',
        'Ocp-Apim-Subscription-Key': subscription_key,
    }
    params = {
        'returnFaceId': 'true',
        'returnFaceLandmarks': 'false',
        'returnFaceAttributes': 'age,gender,headPose,smile,facialHair,glasses,emotion,hair,makeup,occlusion,accessories,blur,exposure,noise',
    }
    body = {'url': url}

    try:
        response = requests.request('POST', uri_base + '/face/v1.0/detect', json=body, data=None, headers=headers, params=params)
        parsed = json.loads(response.text)
        print("\tIn this picture : %s\nWe found that:\n" % url)
        #print (json.dumps(parsed, sort_keys=True, indent=2))
        print("\tThere are %i people" % parsed.__len__())
        for person in parsed:
            print("\t> Person %i:\n\tThis is a %i-year old %s" %(parsed.index(person)+1, person["faceAttributes"]["age"],person["faceAttributes"]["gender"]))
            if int(person["faceAttributes"]["hair"]["bald"]) == 0:
                if is_male(person["faceAttributes"]["gender"]):
                    print("\tHis face, has the id %s" % (person['faceId']))
                else:
                    print("\tHer face, has the id %s"% (person['faceId']))
            return person["faceId"]
    except Exception as e:
        print('Error:')
        print(e)

def recogn(KEY, img_url):
    CF.Key.set(KEY)
    BASE_URL = 'https://centralus.api.cognitive.microsoft.com/face/v1.0/'
    CF.BaseUrl.set(BASE_URL)
    detected = CF.face.detect(img_url)
    print(detected)
    def getRectangle(faceDictionary):
        rect = faceDictionary['faceRectangle']
        left = rect['left']
        top = rect['top']
        bottom = left + rect['height']
        right = top + rect['width']
        return ((left, top), (bottom, right))

    response = requests.get(img_url)
    img = Image.open(BytesIO(response.content))

    draw = ImageDraw.Draw(img)
    for face in detected:
        draw.rectangle(getRectangle(face), outline='blue')

    img.show()

def create_group(person_group_id, key, user_data = None):
    subscription_key = key
    uri_base = 'https://centralus.api.cognitive.microsoft.com'
    name = person_group_id
    headers = {
        'Content-Type': 'application/json',
        'Ocp-Apim-Subscription-Key': subscription_key,
    }
    params = {
        'personGroupId': person_group_id,
    }
    body = {
        'name': name,
        'userData': user_data,
    }

    try:
       response = requests.request('PUT', uri_base + '/face/v1.0/persongroups/' + name, json=body, data=None, headers=headers, params=params)
       parsed = json.loads(response.text)
       print (json.dumps(parsed, sort_keys=True, indent=2))
    except Exception as e:
        print('Error:')
        print(e)


def create_person(person_group_id, person_id, key, user_data = "None"):
    subscription_key = key
    uri_base = 'https://centralus.api.cognitive.microsoft.com'

    headers = {
        'Content-Type': 'application/json',
        'Ocp-Apim-Subscription-Key': subscription_key,
    }
    params = {
        'personGroupId': person_group_id,
    }
    body = {
        "name": person_id,
        "userData": user_data,
    }

    try:
       response = requests.request('POST', uri_base + '/face/v1.0/persongroups/' + person_group_id + '/persons', json=body, data=None, headers=headers, params=params)
       parsed = json.loads(response.text)
       #print (json.dumps(parsed, sort_keys=True, indent=2))
       return parsed["personId"]
    except Exception as e:
        print('Error:')
        print(e)

def add_face(img_url, person_group_id, person_id, key, user_data = None, target_face = None):
    subscription_key = key
    uri_base = 'https://centralus.api.cognitive.microsoft.com'

    headers = {
        'Content-Type': 'application/json',
        'Ocp-Apim-Subscription-Key': subscription_key,
    }
    params = {
        'userData': user_data,
        'targetFace': target_face,
    }
    body = {
        'url': img_url,
    }
    
    try:
       response = requests.request('POST', uri_base + '/face/v1.0/persongroups/' + person_group_id + '/persons/' + person_id + '/persistedFaces', json=body, data=None, headers=headers, params=params)
       parsed = json.loads(response.text)
       #print (json.dumps(parsed, sort_keys=True, indent=2))
       #print(parsed["persistedFaceId"])
    except Exception as e:
        print('Error:')
        print(e)

def train_group(person_group_id, key):
    subscription_key = key
    uri_base = 'https://centralus.api.cognitive.microsoft.com'

    headers = {
        'Ocp-Apim-Subscription-Key': subscription_key,
    }
    params = {
        'personGroupId': person_group_id,
    }
    body = {}

    try:
       requests.request('POST', uri_base + '/face/v1.0/persongroups/' + person_group_id + '/train', json=body, data=None, headers=headers, params=params)
    except Exception as e:
        print('Error:')
        print(e)


def identify_student(faceIds, person_group_id, key, large_person_group_id = None, max_students_return = 1, threshold = .4):
    subscription_key = key
    uri_base = 'https://centralus.api.cognitive.microsoft.com'

    headers = {
        'Content-Type': 'application/json',
        'Ocp-Apim-Subscription-Key': subscription_key,
    }
    params = {}
    body = {
        'personGroupId': person_group_id,
        'faceIds': faceIds,
        'maxNumOfCandidatesReturned': max_students_return,
        'confidenceThreshold': threshold,
    }
    
    try:
       response = requests.request('POST', uri_base + '/face/v1.0/identify/', json=body, data=None, headers=headers, params=params)
       parsed = json.loads(response.text)
       #print (json.dumps(parsed, sort_keys=True, indent=2))
       for person in parsed:
           return (person['candidates'][0]['personId'])
    except Exception as e:
        print('Error:')
        print(e)

def get_student_name(person_group_id, student_id, key):
    subscription_key = key
    uri_base = 'https://centralus.api.cognitive.microsoft.com'

    headers = {
        'Ocp-Apim-Subscription-Key': subscription_key,
    }
    params = {
        'personGroupId': person_group_id,
        'personId': student_id,
    }
    body = {}

    try:
       response = requests.request('GET', uri_base + '/face/v1.0/persongroups/' + person_group_id + '/persons/' + student_id, json=body, data=None, headers=headers, params=params)
       parsed = json.loads(response.text)
       #print (json.dumps(parsed, sort_keys=True, indent=2))
       return (parsed['name'])
    except Exception as e:
        print('Error:')
        print(e)

def delete_group(person_group_id, key):
    subscription_key = key
    uri_base = 'https://centralus.api.cognitive.microsoft.com'

    headers = {
        'Ocp-Apim-Subscription-Key': subscription_key,
    }
    params = {
        'personGroupId': person_group_id,
    }
    body = {}

    try:
       response = requests.request('DELETE', uri_base + '/face/v1.0/persongroups/' + person_group_id + '/train', json=body, data=None, headers=headers, params=params)
       parsed = json.loads(response.text)
       #print (json.dumps(parsed, sort_keys=True, indent=2))
    except Exception as e:
        print('Error:')
        print(e)

person_group_id = "class-group-id"
create_group(person_group_id, keyVal)

gabiName = "Gabi Norsworthy"
person_id = create_person(person_group_id, gabiName, keyVal)
add_face(gabiURL, person_group_id, person_id, keyVal)

wesName = "Wesley Till"
person_id = create_person(person_group_id, wesName, keyVal)
add_face(wesURL, person_group_id, person_id, keyVal)

landonName = "Landon Creel"
person_id = create_person(person_group_id, landonName, keyVal)
add_face(landonURL, person_group_id, person_id, keyVal)

##### INSERT VIDEO FEED IMAGE IN PLACE OF LANDONURL ####
faceIds = [paraMade(keyVal, landonURL)]
#recogn(keyVal, imgURL)

train_group(person_group_id, keyVal)

#print(faceIds)
student_id = identify_student(faceIds, person_group_id, keyVal)

student_name = get_student_name(person_group_id, student_id, keyVal)

print('\nARE YOU ' + student_name + '?')

delete_group(person_group_id, keyVal)
