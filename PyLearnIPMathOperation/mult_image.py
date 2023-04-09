import cv2
import numpy as np


image_dandan = cv2.imread('input/c.tif')
image_mask = cv2.imread('input/d.tif')

image_dandan = cv2.cvtColor(image_dandan,cv2.COLOR_BGR2GRAY)
image_mask = cv2.cvtColor(image_mask,cv2.COLOR_BGR2GRAY)

image_mask = image_mask/255
image_mask = image_mask.astype(np.uint8)

# result = image_mask * image_dandan
result = cv2.multiply(image_mask,image_dandan)

cv2.imwrite('output/New_dandon.jpg',result)