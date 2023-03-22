import cv2

lady_image = cv2.imread('lady.jpg')
man_image = cv2.imread('man.jpg')

for i in range(lady_image.shape[0]):
    for j in range(lady_image.shape[1]):
        lady_image[i,j] = 255 - lady_image[i,j]
        
for i in range(man_image.shape[0]):
    for j in range(man_image.shape[1]):
        man_image[i,j] = 255 - man_image[i,j]

cv2.imwrite('lady_2.jpg',lady_image)
cv2.imwrite('man_2.jpg',man_image)