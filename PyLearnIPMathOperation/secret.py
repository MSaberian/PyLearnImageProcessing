import cv2
import numpy as np

secret_0 = cv2.imread('input/secret_0.jpg')
secret_1 = cv2.imread('input/secret_1.jpg')

secret = 255 - secret_1 + secret_0

cv2.imwrite('output\sketch.jpg', secret)