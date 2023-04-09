import os
import cv2
import numpy as np

image_1 = cv2.imread('input/d1.bmp')
image_2 = cv2.imread('input/d2.bmp')

result = image_1 - image_2


cv2.imwrite('output\do_it.jpg',result)



