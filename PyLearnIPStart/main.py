import cv2

my_image = cv2.imread('shaldon.png')
my_image_2 = cv2.cvtColor(my_image, cv2.COLOR_BGR2GRAY)

# print(my_image_2[350,20])
# my_image_2[350:370,20:30] = 255
# print(my_image_2.shape)

pepper = my_image_2[530:680,850:970]

my_image_2[0:150,0:120] = pepper
cv2.imshow('none', my_image_2)
cv2.waitKey()
# cv2.imwrite('result.jpg',my_image_2)