import requests
import json
import cv2
import numpy as np

addr = 'http://localhost:5000'
test_url = addr + '/face/send'

# prepare headers for http request
content_type = 'image/jpeg'
headers = {'content-type': content_type}

if __name__ == '__main__':
    img = cv2.imread('data/cat.jpeg')
    # encode image as jpeg
    _, img_encoded = cv2.imencode('.jpeg', img)
    # send http request with image and receive response
    response = requests.post(test_url, data=img_encoded.tostring(), headers=headers)
    # decode response
    print (json.loads(response.text))