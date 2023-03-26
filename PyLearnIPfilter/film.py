import time
import cv2
import numpy as np

while True:
    my_image = np.random.random((250, 350)) * 255
    my_image = np.array(my_image, dtype=np.uint8)

    cv2.imshow('result', my_image)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

print('end')
