import time
import cv2
import numpy as np

TV_image = cv2.imread('media\old_TV.jpg')
TV_image = cv2.cvtColor(TV_image,cv2.COLOR_BGR2GRAY)
rows, cols = TV_image.shape
_, TV_image_thre = cv2.threshold(TV_image, 250, 255, cv2.THRESH_BINARY)
writer = cv2.VideoWriter("media\TV_noise.mp4", cv2.VideoWriter_fourcc(*'XVID'), 40, (cols, rows))

while True:
    noise = np.random.random((230, 300)) * 255
    noise = np.array(noise, dtype=np.uint8)
    noise_TV = noise*TV_image_thre[40:270,70:370] + TV_image[40:270,70:370]
    frame = TV_image
    frame[40:270,70:370] = noise_TV
    frame = cv2.cvtColor(frame, cv2.COLOR_GRAY2BGR)
    writer.write(frame)
    cv2.imshow('old TV', frame)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

writer.release()