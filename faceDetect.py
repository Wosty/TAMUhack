
########### Python 2.7 #############
import http.client
import urllib
import sbase64

headers = {
    # Request headers
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': 'ed9917a2d6584af18fb22e51f6466956',
}

params = urllib.urlencode({
    # Request parameters
    'returnFaceId': 'true',
    'returnFaceLandmarks': 'false',
    'returnFaceAttributes': '',
})

try:
    conn = httplib.HTTPSConnection('southcentralus.api.cognitive.microsoft.com')
    conn.request("POST", "/face/v1.0/detect?%s" % params, "{body}", headers)
    response = conn.getresponse()
    data = response.read()
    print(data)
    conn.close()
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))

####################################