import cv2
import numpy as np

cap = cv2.VideoCapture(0)
# cap = cv2.VideoCapture('Armin.mp4')
_, frame = cap.read()
frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
rows, cols = frame.shape

writer = cv2.VideoWriter('output\mamad.mp4', cv2.VideoWriter_fourcc(*'MJPG'), 10, (cols, rows))

while True:
    _, frame_org = cap.read()
    frame_org = cv2.cvtColor(frame_org, cv2.COLOR_BGR2GRAY)
    frame_detect = frame_org[(rows//2 - 100):(rows//2 + 100), (cols//2 - 100):(cols//2 + 100)]
    frame_filtered = cv2.fastNlMeansDenoising(frame_org, None, 200, 10, 10 )  
    cv2.rectangle(frame_filtered, (cols//2 - 100,rows//2 - 100), (cols//2 + 100,rows//2 + 100), 0,8)
    mean = np.mean(frame_detect)
    if mean > 150:
        color = 'White'
    elif mean < 80:
        color = 'Black'
    else:
        color = 'Gray'
    cv2.putText(frame_filtered, color, (cols//2 - 60,rows//2 - 120), cv2.FONT_HERSHEY_SIMPLEX, 1, 0, thickness= 2)
    frame_filtered[(rows//2 - 100):(rows//2 + 100), (cols//2 - 100):(cols//2 + 100)] = frame_detect
    frame = cv2.cvtColor(frame_filtered, cv2.COLOR_GRAY2BGR)
    writer.write(frame)
    cv2.imshow('result', frame)
    if cv2.waitKey(5) & 0xFF == ord('q'):
        break

writer.release()
cap.release()
cv2.destroyAllWindows()
