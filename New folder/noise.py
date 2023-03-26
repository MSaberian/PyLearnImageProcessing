import cv2
import numpy as np
# import numpy as mamad

my_image = np.ones((500, 800), dtype=np.uint8) * 255

# my_image = np.random.random((250, 350)) * 255
# my_image = np.array(my_image, dtype=np.uint8)

cv2.rectangle(my_image, (23,35), (700, 450), 40,20)

cv2.circle(my_image, (600, 200), (120), 200, 10)

cv2.line(my_image, (100, 100), (700, 150), 150, 15)

cv2.putText(my_image, 'mamad', (200, 200), cv2.FONT_HERSHEY_SIMPLEX, 2, 100)

cv2.imshow('result', my_image)
cv2.waitKey()
