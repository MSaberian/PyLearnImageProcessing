import random
import cv2
import numpy as np

width = 400
lenght = 700
football_pitch_image = np.ones((width,lenght,3))
football_pitch_image = np.array(football_pitch_image, dtype=np.uint8)
noise = np.random.random((width, lenght)) * 100
grass = np.array(noise, dtype=np.uint8)

for i in range(7):
    football_pitch_image[:,(i*100):(i*100 + 100),1] = 100 + ((i+1)%2)*50

football_pitch_image[:,:,1] -= grass

cv2.rectangle(football_pitch_image, (30,30), (lenght - 30,width - 30), (255,255,255),4)
cv2.rectangle(football_pitch_image, (30,110), (140,width - 110), (255,255,255),4)
cv2.rectangle(football_pitch_image, (30,150), (80,width - 150), (255,255,255),4)
cv2.rectangle(football_pitch_image, (lenght - 30,110), (lenght - 140,width - 110), (255,255,255),4)
cv2.rectangle(football_pitch_image, (lenght - 30,150), (lenght - 80,width - 150), (255,255,255),4)
cv2.circle(football_pitch_image, (lenght//2,width//2), 70, (255,255,255),4)
cv2.circle(football_pitch_image, (lenght//2,width//2), 0, (255,255,255),15)
cv2.line(football_pitch_image, (lenght//2,30), (lenght//2,width-30), (255,255,255),4)


cv2.imshow('football pitch',football_pitch_image)
cv2.imwrite('output\Football_pitch.jpg',football_pitch_image)
cv2.waitKey()