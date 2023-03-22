import cv2
import numpy as np

mans_image = cv2.imread('mans.jpg')
mans_image = cv2.cvtColor(mans_image, cv2.COLOR_BGR2GRAY)
mans_image_2 = np.zeros((mans_image.shape[0], mans_image.shape[1]))

for i in range(mans_image.shape[0]):
    for j in range(mans_image.shape[1]):
        mans_image_2[i,j] = mans_image[mans_image.shape[0] - i -1,mans_image.shape[1] - j -1]
       
cv2.imwrite('mans_2.jpg',mans_image_2)