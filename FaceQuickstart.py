# <Subscription Key> == value of my key
# may need to change BASE_URL to correct region identiier
# img_url to URL of any image you'd like to use

import cognitive_face as CF

KEY = 'ed9917a2d6584af18fb22e51f6466956'
CF.Key.set(KEY)

#BASE_URL = 'https://southcentralus.api.cognitive.microsoft.com/face/v1.0'
BASE_URL = 'https://southcentralus.api.cognitive.microsoft.com/face/v1.0/detect? \
returnFaceId=tru&returnFaceLandmarks=false'
CF.BaseUrl.set(BASE_URL)

img_url = 'https://raw.githubusercontent.com/Microsoft/Cognitive-Face-Windows/master/Data/detection1.jpg'
faces = CF.face.detect(img_url)
print(faces)
