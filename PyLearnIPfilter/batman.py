import cv2

image = cv2.imread('media\Bat.jpg')
image_org = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

# cv2.imshow('result',image_org[250:350,300:700])

_, image_thre = cv2.threshold(image_org, 135, 255, cv2.THRESH_BINARY_INV)
# cv2.imshow('threshold 135',image)

_, image = cv2.threshold(image_org, 175, 255, cv2.THRESH_BINARY_INV)
# cv2.imshow('threshold 175',image[250:350,300:700])
image = cv2.fastNlMeansDenoising(image, None, 200, 3, 3 )  
# cv2.imshow('fastNlMeansDenoising',image[250:350,300:700])
_, image_denoise = cv2.threshold(image, 175, 255, cv2.THRESH_BINARY)
# cv2.imshow('threshold after filter',image[250:350,300:700])

image_bat = image_thre
image_bat[250:350,400:600] = image_denoise[250:350,400:600]
cv2.putText(image_bat, 'BATMAN', (300, 550), cv2.FONT_HERSHEY_SIMPLEX, 3, 255, thickness= 5)
cv2.imshow('image_bat',image_bat)
cv2.imwrite('media\Batman.jpg',image_bat)
cv2.waitKey()


