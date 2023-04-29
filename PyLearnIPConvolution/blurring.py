import cv2
import numpy as np

image = cv2.imread('input/flower.jpg', cv2.IMREAD_GRAYSCALE)
image = image[500:700,500:700]
rows, cols = image.shape
FS = 39 # filter size
print(image.shape)
image_new = np.zeros((rows, cols)) 

# filter = np.array([[-1, 0, 1],
#                    [-1, 0, 1],
#                    [-1, 0, 1]])
filter = np.ones((FS,FS))/(FS*FS)

for i in range(FS//2, rows-FS//2):
    print(i, end=', ')
    for j in range(FS//2, cols-FS//2):
        small = image[(i-FS//2):(i+FS//2+1),(j-FS//2):(j+FS//2+1)]
        average = np.sum(filter * small)
        if average <128 or image[i,j] < 128:
            if average > 42: 
                small[small>32] = 16
                average2 = np.sum(filter * small)
                image_new[i, j] = average2
            else:
                image_new[i, j] = average
        else:
            image = cv2.imread('input/flower.jpg', cv2.IMREAD_GRAYSCALE)
            image = image[500:700,500:700]
            image_new[i, j] = image[i,j]
        
cv2.imwrite('output/flower_blur4.png',image_new)
cv2.imwrite('output/imageorg.png',image)

# cv2.waitKey()