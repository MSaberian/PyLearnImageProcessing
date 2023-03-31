import cv2
import numpy as np

landscape_image = cv2.imread('media\landscape.jpg')
landscape_snow_image = cv2.cvtColor(landscape_image,cv2.COLOR_BGR2GRAY)
rows, cols = landscape_snow_image.shape
writer = cv2.VideoWriter("media\landscape_snow_new.mp4", cv2.VideoWriter_fourcc(*'XVID'), 40, (cols, rows))

snows = []
for i in range(5):
    noise = np.random.random((rows, cols)) * 255
    snows.append(np.array(noise, dtype=np.uint8))

def shift(Array, directionX= None, directionY= None, rangeX= (0,0), rangeY= (0,0)):
    Array_org = Array
    result = np.zeros(Array.shape)
    
    if directionX != None:
        shiftX = directionX
    elif rangeX[0] != 0 or rangeX[1] != 0:
        shiftX = np.random.randint(rangeX[0],rangeX[1] + 1)

    if directionY != None:
        shiftY = directionY
    elif rangeY[0] != 0 or rangeY[1] != 0:
        shiftY = np.random.randint(rangeY[0],rangeY[1] + 1)
    
    if shiftX > 0:
        result[:,0] = Array_org[:,-1]
        if shiftX > 1:
            result[:,1:shiftX] = Array_org[:,-1*shiftX:-1]
        result[:,shiftX:] = Array_org[:,:(-1*shiftX)]
        Array_org = result

    if shiftX < 0:
        result[:,-1] = Array_org[:,0]
        if shiftY < -1:
            result[:,shiftX:-1] = Array_org[:,0:(-1*shiftX)]
        result[:,:shiftX] = Array_org[:,(-1*shiftX):]
        Array_org = result

    if shiftY > 0:
        result[0,:] = Array_org[-1,:]
        if shiftY > 1:
            result[1:shiftY,:] = Array_org[-1*shiftY:-1,:]
        result[shiftY:,:] = Array_org[:(-1*shiftY),:]
        Array_org = result

    if shiftY < 0:
        result[-1,:] = Array_org[0,:]
        if shiftY < -1:
            result[shiftY:-1,:] = Array_org[0:(-1*shiftY),:]
        result[:shiftY,:] = Array_org[(-1*shiftY):,:]
        Array_org = result

    return result

while True:
    landscape_snow_image = cv2.cvtColor(landscape_image,cv2.COLOR_BGR2GRAY)
    for i in range(len(snows)):
        snows[i] = shift(snows[i], directionY= 1, rangeX= (-2,2))
        landscape_snow_image[snows[i] > 252] = 255
    frame = cv2.cvtColor(landscape_snow_image, cv2.COLOR_GRAY2BGR)
    writer.write(frame)
    cv2.imshow('landscape_snow', frame)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

writer.release()