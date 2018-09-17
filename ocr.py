from PIL import Image
import numpy as np
import requests
import cv2
import pytesseract
import os

urls = [
    # images that have seed
    "https://i.redd.it/y739y7arcmm11.jpg", # clean gameplay
    # "https://i.redd.it/uv59t054cjm11.jpg", # clean gameplay
    # "https://i.redd.it/af6zmilffmm11.jpg", # history screen
    # "https://i.redd.it/80t0y3smljm11.png", # clean gameplay
    # "https://i.redd.it/tckb9kt92pm11.png", # history screen
    # "https://i.redd.it/70ao4b6m4gm11.jpg", # store, contrast line across seed


    # # images that don't
    # "https://i.imgur.com/5nStfv4.png", # people really love
    # "https://i.imgur.com/jl5gtCP.jpg", # making defect fanart
]

def url_to_image(url):
    # download the image, convert it to a NumPy array, and then read
    # it into OpenCV format


    resp = requests.get(url)
    image = np.asarray(bytearray(resp.content), dtype="uint8")
    image = cv2.imdecode(image, cv2.IMREAD_COLOR)

    return image

# loop over the image URLs
for url in urls:
    #download the image URL and display it
    print("downloading %s", url)
    image = url_to_image(url)
    cv2.imshow("Image", image)
    cv2.waitKey(0)
    