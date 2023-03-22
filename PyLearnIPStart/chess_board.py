import cv2
import numpy as np

size = 64
board = np.zeros((size*8, size*8))

for i in range(8):
    for j in range(8):
        for row in range(i*size,(i+1)*size):
            for col in range(j*size,(j+1)*size):
                board[row][col] = ((i+j)%2)*255

cv2.imshow('chess board', board)
cv2.waitKey()

