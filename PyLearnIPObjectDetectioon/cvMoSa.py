import cv2
import numpy as np
import matplotlib.pyplot as plt

def boundingRectMoSa(contour):
    x = np.min(contour[:,0,0])
    w = np.max(contour[:,0,0]) - x + 1
    y = np.min(contour[:,0,1])
    h = np.max(contour[:,0,1]) - y + 1
    return x



