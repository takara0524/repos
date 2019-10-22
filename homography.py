#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 18:24:17 2019

@author: TAKARA
"""

import cv2
import numpy as np

from IPython.display import display, Image

def display_cv_image(image, formats='.png'):
    decoded_bytes = cv2.imencode(formats, image)[1].tobytes()
    display(Image(data=decoded_bytes))
    
def homography(path, input_img_width, input_img_height, area, area_color, out_img_width, out_img_height):
    
    img = cv2.imread(path)
    img = cv2.resize(img, (input_img_width, input_img_height))
    areas = []
    
    areas.append(area)
    cv2.drawContours(img, areas[0], -1, area_color, 3)
    display_cv_image(img)
    print(areas[0])

    dst = []

    pts1 = np.float32(areas[0])
    pts2 = np.float32([[out_img_width, out_img_height],[out_img_width,0],[0,0],[0,out_img_height]])

    M = cv2.getPerspectiveTransform(pts1,pts2)
    dst = cv2.warpPerspective(img,M,(out_img_width,out_img_height))

    display_cv_image(dst)
    return dst

if __name__ == '__main__':
    path = "./test.png"
    input_img_width = 512
    input_img_height = 512
    area = np.array([[[492, 400], [488, 107], [125, 25], [124, 512]]])
    area_color = (0, 0, 255)
    out_img_width = 650
    out_img_height = 366
    
    homography(path, input_img_width, input_img_height, area, area_color, out_img_width, out_img_height)
    