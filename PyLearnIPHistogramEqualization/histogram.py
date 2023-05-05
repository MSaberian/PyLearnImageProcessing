import cv2
import matplotlib.pyplot as plt

image = cv2.imread('input\lady_2.jpg', cv2.IMREAD_GRAYSCALE)


hist = cv2.calcHist([image], [0], None, [256], [0, 256])
plt.plot(hist)
plt.show()