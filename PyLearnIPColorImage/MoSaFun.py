import cv2
import numpy as np
import matplotlib.pyplot as plt

def color2gray(image):
    result = np.mean(image, axis=2)
    return result
