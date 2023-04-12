import cv2
import numpy as np

image_one = cv2.imread(f'input/Black_hole/1/1.jpg')
image_black_holes = []
for i in range(4):
    image_black_holes_quarter = np.zeros(image_one.shape,np.float32)
    for j in range(5):
        image_black_holes_quarter +=cv2.imread(f'input\Black_hole\{i+1}\{j+1}.jpg').astype(np.float32)
    image_black_holes_quarter = (image_black_holes_quarter/5).astype(np.uint8)
    image_black_holes.append(image_black_holes_quarter)

image_black_holes_row_0 = np.concatenate((image_black_holes[0], image_black_holes[1]), axis=1)
image_black_holes_row_1 = np.concatenate((image_black_holes[2], image_black_holes[3]), axis=1)
image_black_hole = np.concatenate((image_black_holes_row_0, image_black_holes_row_1), axis=0)

cv2.imwrite('output\image_black_hole.jpg',image_black_hole)