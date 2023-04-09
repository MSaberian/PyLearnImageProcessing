import os
import cv2
import numpy as np

image_1 = cv2.imread('input/a.tif')
image_2 = cv2.imread('input/b.tif')

# image_1 = image_1.astype(np.float32)
# image_1 = image_1.astype(np.float32)

# result = image_1 - image_2
result = cv2.subtract(image_1, image_2) * 5
# result = 255 - result


cv2.imwrite('output\c.jpg',result)



