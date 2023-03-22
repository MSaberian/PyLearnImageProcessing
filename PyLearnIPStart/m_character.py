import cv2
import numpy as np

m_character = np.zeros((8, 9))

m_character[0:8,0:9] = 255

m_character[1:7,1] = 0 
m_character[1:7,7] = 0 

for i in range(2,5):
    m_character[i,i] = 0
    m_character[5-i,3+i] = 0

cv2.imwrite('m_character.jpg',m_character)