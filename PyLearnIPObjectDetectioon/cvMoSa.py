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
        temp_area = 0
        temp_points = []
        last_state = False
        for j in range(y, y+h):
            if ([i, j] in contour_):
                if not last_state:
                    cross +=1
                last_state = True
            elif last_state:
                last_state = False
                if i:
                    if [i-1, j] in points:
                        cross = 1
                    else:
                        cross = 0
            else:
                last_state = False
            if cross % 2 == 1:
                temp_area +=1
                temp_points.append([i,j])
            else:
                if(temp_area):
                    for k in range(temp_area):
                        points.append(temp_points[k])
                area += temp_area
                temp_area = 0
                temp_points = []

    return area, points
