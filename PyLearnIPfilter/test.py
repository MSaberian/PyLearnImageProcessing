import numpy as np

# def shift(Array, directionX= None, directionY= None, rangeX= (0,0), rangeY= (0,0)):
#     Array_org = Array
#     if rangeX[0] != 0 or rangeX[1] != 0:
x= np.zeros(10)
for i in range(10):
    x[i]  = i

print(x[0:-1])
