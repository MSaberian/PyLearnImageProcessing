import cv2

image_mamad = cv2.imread('input\mamad2.jpg', 0)

image_mamad_inverted = 255 - image_mamad
blurred = cv2.GaussianBlur(image_mamad_inverted, (21, 21), 0)
inverted_blurred = 255 - blurred

sketch = image_mamad / inverted_blurred
sketch = sketch * 255

cv2.imwrite('output\sketch.jpg', sketch)