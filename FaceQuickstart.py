# <Subscription Key> == value of my key
# may need to change BASE_URL to correct region identiier
# img_url to URL of any image you'd like to use

import cognitive_face as CF

KEY = 'ed9917a2d6584af18fb22e51f6466956'
CF.Key.set(KEY)

BASE_URL = 'https://southcentralus.api.cognitive.microsoft.com/face/v1.0'
CF.BaseUrl.set(BASE_URL)

img_url = 'https://www.dropbox.com/s/s84x96au7utietc/gabiUIN.jpg?dl=0'
faces = CF.face.detect(img_url)
print(faces)
