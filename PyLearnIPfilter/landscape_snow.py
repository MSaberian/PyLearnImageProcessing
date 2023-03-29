import cv2
import numpy as np

landscape_image = cv2.imread('media\landscape.jpg')
landscape_snow_image = cv2.cvtColor(landscape_image,cv2.COLOR_BGR2GRAY)
rows, cols = landscape_snow_image.shape
writer = cv2.VideoWriter("media\landscape_snow.mp4", cv2.VideoWriter_fourcc(*'XVID'), 40, (cols, rows))
noise = np.random.random((rows, cols)) * 255
noise = np.array(noise, dtype=np.uint8)
snow = noise

while True:
    snow[0,:] = noise[-1,:]
    snow[1:,:] = noise[:-1,:]
    noise = snow
    landscape_snow_image = cv2.cvtColor(landscape_image,cv2.COLOR_BGR2GRAY)
    mmjgjjm = landscape_snow_image
    mmjgjjm[snow > 250] = 255
    frame = cv2.cvtColor(mmjgjjm, cv2.COLOR_GRAY2BGR)
    writer.write(frame)
    cv2.imshow('landscape_snow', frame)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

writer.release()