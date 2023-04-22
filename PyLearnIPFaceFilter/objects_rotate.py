import numpy as np
import cv2
import tensorflow as tf
from functools import partial
from TFLiteFaceDetector import UltraLightFaceDetecion
from TFLiteFaceAlignment import CoordinateAlignmentModel


fd = UltraLightFaceDetecion("weights/RFB-320.tflite", conf_threshold=0.88)
fa = CoordinateAlignmentModel("weights/coor_2d106.tflite")

f = 1.5
lips_numbers = [52, 64, 63, 71, 67, 68, 61, 58, 59, 53, 56, 55]
eyeL_numbers = [35, 41, 40, 42, 39, 37, 33, 36]
eyeR_numbers = [89, 95, 94, 96, 93, 91, 87, 90]

def rotate_effect(object_numbers, mamad_image):
    landmarks = []
    for i in object_numbers:
        landmarks.append(pred[i])
    landmarks = np.array(landmarks, dtype= np.int32)

    x, y, w, h = cv2.boundingRect(landmarks)
    mask = np.zeros(mamad_image.shape, dtype= np.uint8)
    cv2.drawContours(mask, [landmarks], -1, (1,1,1), -1)

    mamad_object = mamad_image * mask
    mamad_object = mamad_object[y:y+h, x:x+w]
    mask = mask[y:y+h, x:x+w]

    mamad_object_big = cv2.resize(mamad_object, (0, 0), fx=f, fy=f)
    mask_object_big = cv2.resize(mask, (0, 0), fx=f, fy=f)

    mamad_object_big = cv2.flip(mamad_object_big, 0)
    mask_object_big = cv2.flip(mask_object_big, 0)
    
    mamad_object_image = np.zeros(mamad_image.shape, dtype= np.uint8)
    mask_object_image = np.zeros(mamad_image.shape, dtype= np.uint8)
    
    x1 = np.int32(x-(f-1)*w//2)
    x2 = x1 + mamad_object_big.shape[1]
    y1 = np.int32(y-(f-1)*h//2)
    y2 = y1 + mamad_object_big.shape[0]
    mamad_object_image[y1:y2, x1:x2] = mamad_object_big
    mask_object_image[y1:y2, x1:x2] = mask_object_big

    mamad_result = mamad_object_image + mamad_image * (1 - mask_object_image)

    return mamad_result

mamad_image = cv2.imread('input/2.jpg')

boxes, scores = fd.inference(mamad_image)

for pred in fa.get_landmarks(mamad_image, boxes):
    for i, p in enumerate(np.round(pred).astype(np.int32)):
        color = (255*(i%3==2), 255*(i%3==0), 255*(i%3==1))
        # cv2.circle(mamad_image, tuple(p), 2, color, -1)
        # cv2.putText(mamad_image, str(i), tuple(p), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color)

mamad_result = rotate_effect(lips_numbers, mamad_image)
mamad_result = rotate_effect(eyeL_numbers, mamad_result)
mamad_result = rotate_effect(eyeR_numbers, mamad_result)

mamad_result = cv2.flip(mamad_result, 0)

cv2.imshow("mamad result", mamad_result)
cv2.imwrite('output/mamad rotate result.jpg',mamad_result)
cv2.waitKey()