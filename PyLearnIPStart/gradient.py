import cv2
import numpy as np

gradient = np.zeros((256, 256))

for i in range(256):
    gradient[i,0:256] = 255 - i

cv2.imwrite('gradient.jpg',gradient)