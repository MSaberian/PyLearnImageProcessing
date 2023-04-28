import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread('input\Mona_Lisa_2.jpg', cv2.IMREAD_GRAYSCALE)

def histogram(image):
    Histogram = np.zeros(256, dtype=np.uint64)
    values, counts = np.unique(image, return_counts=True)
    for num in values:
        Histogram[num] = counts[np.where(values == num)[0]]
    
    return Histogram

result = histogram(image)
# plt.plot(result)
# plt.title('plot')
# plt.xlabel('Intensity value')
# plt.ylabel('Count')
plt.bar(np.arange(0, 256) ,result)
plt.title('bar')
plt.xlabel('Intensity value')
plt.ylabel('Count')
# plt.hist(image.ravel(),256,[0,256], facecolor='blue')
# plt.title('histogram')
# plt.xlabel('Intensity value')
# plt.ylabel('Count')
plt.show()