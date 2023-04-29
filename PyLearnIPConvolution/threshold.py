import cv2
import numpy as np

image = cv2.imread('input/flower.jpg', cv2.IMREAD_GRAYSCALE)

_, image_thre = cv2.threshold(image, 135, 255, cv2.THRESH_BINARY_INV)

cv2.imshow("apple result", image_thre)
cv2.waitKey()