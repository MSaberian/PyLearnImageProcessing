import cv2
import numpy as np

image_sajjad = cv2.imread('input/sajjad.jpg')
image_lion = cv2.imread('input/lion.jpg')

image_sajjad = cv2.cvtColor(image_sajjad,cv2.COLOR_BGR2GRAY)
image_lion = cv2.cvtColor(image_lion,cv2.COLOR_BGR2GRAY)


image_sajjad = image_sajjad.astype(np.float32)
image_lion = image_lion.astype(np.float32)
# result = cv2.add(image_sajjad, image_lion)
# result = np.add(image_human, image_horse)

result = image_sajjad*2/3 + image_lion*1/3

result = result.astype(np.uint8)

# cv2.imshow('football pitch',result)
cv2.imwrite('output\Result_mean.jpg',result)
# cv2.waitKey()