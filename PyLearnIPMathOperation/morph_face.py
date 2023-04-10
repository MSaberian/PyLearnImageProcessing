import cv2
import numpy as np

image_robert = cv2.imread('input/robert4.jpg')
image_mamad = cv2.imread('input/mamad3.jpg')
image_mamad = image_mamad[10:,:,:]
w, h, _ = image_mamad.shape
image_robert = cv2.resize(image_robert, [h, w])

image_robert = image_robert.astype(np.float32)
image_mamad = image_mamad.astype(np.float32)

image_mamad_robert1 = image_robert*.25 + image_mamad*.75
image_mamad_robert2 = image_robert*.5 + image_mamad*.5
image_mamad_robert3 = image_robert*.75 + image_mamad*.25

image_mamad_robert1 = image_mamad_robert1.astype(np.uint8)
image_mamad_robert2 = image_mamad_robert2.astype(np.uint8)
image_mamad_robert3 = image_mamad_robert3.astype(np.uint8)

image_mamad_robert = np.concatenate((image_mamad, image_mamad_robert1, image_mamad_robert2,
 image_mamad_robert3, image_robert), axis=1)

cv2.imwrite('output/mamad_robert.jpg',image_mamad_robert)