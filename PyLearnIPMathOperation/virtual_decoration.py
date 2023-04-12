import cv2
import numpy as np

image_floor = cv2.imread('input/floor.jpg')
image_new_floor = cv2.imread('input/new_floor.jpg')
image_room = cv2.imread('input/room_background.jpg')
image_room0 = image_room

image_floor = image_floor / 255

image_room0 = image_room0*(1-image_floor)

result = np.zeros(image_floor.shape)

result = image_floor*image_new_floor + image_room0

cv2.imwrite('output/New_room.jpg',result)
result = cv2.resize(result, [result.shape[1]//3, result.shape[0]//3])
image_floor = cv2.resize(image_floor, [image_floor.shape[1]//3, image_floor.shape[0]//3])
cv2.imwrite('output/floor_small.jpg',image_floor*255)
image_new_floor = cv2.resize(image_new_floor, [image_new_floor.shape[1]//3, image_new_floor.shape[0]//3])
cv2.imwrite('output/new_floor_small.jpg',image_new_floor)
image_room = cv2.resize(image_room, [image_room.shape[1]//3, image_room.shape[0]//3])
cv2.imwrite('output/room_small.jpg',image_room)

image_row_0 = np.concatenate((image_floor*255, image_new_floor), axis=1)
image_row_1 = np.concatenate((image_room, result), axis=1)
room_concatenate = np.concatenate((image_row_0, image_row_1), axis=0)
cv2.imwrite('output/room_concatenate.jpg',room_concatenate)