import numpy as np
import cv2
import tensorflow as tf
from functools import partial
import time
from TFLiteFaceDetector import UltraLightFaceDetecion
from TFLiteFaceAlignment import CoordinateAlignmentModel

def zoom_effect(landmark):

    return result

fd = UltraLightFaceDetecion("weights/RFB-320.tflite", conf_threshold=0.88)
fa = CoordinateAlignmentModel("weights/coor_2d106.tflite")

image = cv2.imread('input/6.jpg')

start_time = time.perf_counter()

boxes, scores = fd.inference(image)

for pred in fa.get_landmarks(image, boxes):
    for i, p in enumerate(np.round(pred).astype(np.int32)):
        color = (255*(i%3==0), 255*(i%3==1), 255*(i%3==2))
        # cv2.circle(image, tuple(p), 2, color, -1)
        # cv2.putText(image, str(i), tuple(p), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color)

    lips_landmarks = []
    for i in [52, 64, 63, 71, 67, 68, 61, 58, 59, 53, 56, 55]:
        lips_landmarks.append(pred[i])
    lips_landmarks = np.array(lips_landmarks, dtype= np.int32)
    # print(lips_landmarks)

    x, y, w, h = cv2.boundingRect(lips_landmarks)
    mask = np.zeros(image.shape, dtype= np.uint8)
    cv2.drawContours(mask, [lips_landmarks], -1, (255,255,255), -1)
    cv2.imshow("mask", mask)
    mask = mask // 255

    result = image * mask
    result = result[y:y+h, x:x+w]

    result_big = cv2.resize(result, (0, 0), fx=4, fy=4)

cv2.imshow("image", image)
cv2.imshow("result", result_big)
cv2.imwrite('output\Result.jpg',result_big)
cv2.waitKey()