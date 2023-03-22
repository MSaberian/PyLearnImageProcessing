import cv2
import numpy as np

Mona_Lisa_image = cv2.imread('Mona_Lisa.jpg')
Mona_Lisa_image = cv2.cvtColor(Mona_Lisa_image, cv2.COLOR_BGR2GRAY)

size = Mona_Lisa_image.shape[1]//3
width = 120

for i in range(size):
    Mona_Lisa_image[i,(size-width-i):(size+width-i)] = 0
    
for i in range(width*2):
    Mona_Lisa_image[(size-width-i):(size+width-i),i] = 0
       
cv2.imwrite('Mona_Lisa_2.jpg',Mona_Lisa_image)