#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 18:24:17 2019

@author: TAKARA
"""

import cv2
import numpy as np
from PIL import Image

from IPython.display import display, Image

def display_cv_image(image, formats='.png'):
    decoded_bytes = cv2.imencode(formats, image)[1].tobytes()
    display(Image(data=decoded_bytes))
    
def homography(name):
    img = cv2.imread(name)
    img = cv2.resize(img, (512, 512))
    #display_cv_image(img)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    ret, th1 = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)
    #display_cv_image(th1)

    contours, hierarchy = cv2.findContours(th1, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    areas = []
    """
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 10000:
            epsilon = 0.1*cv2.arcLength(cnt, True)
            approx = cv2.approxPolyDP(cnt, epsilon, True)
            areas.append(approx)
    """
    areas.append(np.array([[[492, 400], [488, 107], [125, 25], [124, 512]]]))
    cv2.drawContours(img, areas[0], -1, (0, 0, 255), 3)
    display_cv_image(img)
    print(areas[0])
    img = cv2.imread(name)
    img = cv2.resize(img, (512, 512))
    dst = []

    pts1 = np.float32(areas[0])
    pts2 = np.float32([[650,366],[650,0],[0,0],[0,366]])

    M = cv2.getPerspectiveTransform(pts1,pts2)
    dst = cv2.warpPerspective(img,M,(650,366))

    display_cv_image(dst)
    return dst

if __name__ == "__main__":
    path = "./TestImage/test008/raw現像2/"
    out = "./TestImage/test008/"
    for d in range(120, 260, 10):
        name = path + str(d) + ".png"
        i = homography(name)
        name = out + str(d) + ".png"
        cv2.imwrite(name, i)