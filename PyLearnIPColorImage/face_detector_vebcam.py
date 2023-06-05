import cv2
import numpy as np


cap = cv2.VideoCapture(0)
_, frame = cap.read()
rows, cols, _ = frame.shape
writer = cv2.VideoWriter('output\mamad1.mp4', cv2.VideoWriter_fourcc(*'MJPG'), 8, (600, 600))

image_girl = cv2.imread('input\girl.jpg')
image_girl = cv2.resize(image_girl, (600, 600))

image_Salvator = cv2.imread('input\Salvator_Mundi.jpg')
image_Salvator = cv2.resize(image_Salvator, (600, 600))
image_Salvator_org = image_Salvator

image_Eren = cv2.imread('input\Eren_Yeager.jpg')
image_Eren = cv2.resize(image_Eren, (600, 600))

image_Mona = cv2.imread('input\Mona_Lisa.jpg')
image_Mona = cv2.resize(image_Mona, (600, 600))

image_Sherlock = cv2.imread('input\Sherlock.jpg')
image_Sherlock = cv2.resize(image_Sherlock, (600, 600))

choice = 1

while True:
    _, frame = cap.read()
    frame = cv2.flip(frame, 1)

    if choice == 1:
        image_girl[220:300,170:350] = frame[220:300,170:350]        
        frame = image_girl

    elif choice == 2:
        image_Salvator[300:,0:120] = frame[-300:,0:120]  
        frame = image_Salvator

    elif choice == 3:
        image_Eren[280:420,70:240] = frame[280:420,70:240]
        frame = image_Eren

    elif choice == 4:
        image_Mona[400:460,200:350] = frame[400:460,200:350]
        frame = image_Mona

    elif choice == 5:
        image_Sherlock[350:530,150:320] = frame[250:430,150:320]
        frame = image_Sherlock

    elif choice == 0:
        ...

    writer.write(frame)
    cv2.imshow('mamad',frame)
    choice1 = cv2.waitKey(5)
    if choice1 & 0xFF == ord('q'):
        break
    elif choice1 & 0xFF == ord('1'):
        choice = 1
    elif choice1 & 0xFF == ord('2'):
        choice = 2
    elif choice1 & 0xFF == ord('3'):
        choice = 3
    elif choice1 & 0xFF == ord('4'):
        choice = 4
    elif choice1 & 0xFF == ord('5'):
        choice = 5
    elif choice1 & 0xFF == ord('6'):
        choice = 6

writer.release()
cap.release()
cv2.destroyAllWindows()


