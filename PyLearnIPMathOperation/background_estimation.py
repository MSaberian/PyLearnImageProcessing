import numpy as np
import cv2
from skimage import data, filters
 
cap = cv2.VideoCapture('input/road.mp4')
 
frameIds = cap.get(cv2.CAP_PROP_FRAME_COUNT) * np.random.uniform(size=25)


frames = []
for fid in frameIds:
    cap.set(cv2.CAP_PROP_POS_FRAMES, fid)
    ret, frame = cap.read()
    frames.append(frame)
 
medianFrame = np.median(frames, axis=0).astype(dtype=np.uint8)    
 
cv2.imwrite('output/road.jpg', medianFrame)
cv2.imshow('frame', medianFrame)
cv2.waitKey(0)