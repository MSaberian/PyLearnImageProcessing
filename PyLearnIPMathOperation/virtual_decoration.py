import cv2
import numpy as np

image_floor = cv2.imread('input/floor.jpg')
image_new_floor = cv2.imread('input/new_floor.jpg')
image_room = cv2.imread('input/room_background.jpg')

image_floor = image_floor / 255

image_room = image_room*(1-image_floor)

result = np.zeros(image_floor.shape)

result = image_floor*image_new_floor + image_room


cv2.imwrite('output/New_room.jpg',result)