import cv2
import numpy as np

size = 64
board = np.zeros((size*8, size*8))

for i in range(8):
    for j in range(8):
        board[i*size:(i+1)*size,j*size:(j+1)*size] = ((i+j)%2)*255

cv2.imshow('chess board', board)
cv2.waitKey()