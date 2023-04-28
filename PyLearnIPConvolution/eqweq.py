import cv2
import numpy as np

image = cv2.imread('input\old_TV.jpg', cv2.IMREAD_GRAYSCALE)
rows, cols = image.shape
print(image.shape)
image_new = np.zeros((rows, cols))

filter = np.array([[-1, 0, 1],
                   [-1, 0, 1],
                   [-1, 0, 1]])
# filter = np.ones((7,7))/49

for i in range(1, rows-1):
    print(i, end=', ')
    for j in range(1, cols-1):
        small = image[i-1:i+2,j-1:j+2]
        # average = np.sum(small)/9
        average = np.sum(filter * small)
        image_new[i, j] = average

cv2.imshow("apple result", image_new)
cv2.imwrite('output/resad.png',image_new)

cv2.waitKey()