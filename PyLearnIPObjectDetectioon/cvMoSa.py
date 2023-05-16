import cv2
import numpy as np
import matplotlib.pyplot as plt


def boundingRectMoSa(contour):
    x = np.min(contour[:,0,0])
    w = np.max(contour[:,0,0]) - x + 1
    y = np.min(contour[:,0,1])
    h = np.max(contour[:,0,1]) - y + 1
    return x, y, w, h

def contourAreaMoSa(contour):

    x, y, w, h = boundingRectMoSa(contour)
    contour_ = contour[:,0].tolist()
    area = 0
    points = []
    for i in range(x, x+w):
        cross = 0
        for j in range(y, y+h):
            point = [i, j]  
            print(point in contour_)
            
            # if big and small:
            #     area += 1
            #     points.append([i, j])

    return area, points
