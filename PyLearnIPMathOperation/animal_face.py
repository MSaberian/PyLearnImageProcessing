import cv2
import numpy as np

image_tiger = cv2.imread('input/tiger1.jpg')
image_mamad = cv2.imread('input/mamad.jpg')
image_tiger = cv2.resize(image_tiger, [640, 640])

def transparent_sticker(sticker):
    rows, cols, _ = sticker.shape
    sticker_ghost = np.zeros(sticker.shape)
    sticker_transparent = np.zeros(sticker.shape)
    sticker_ghost = np.array(sticker_ghost, dtype=np.uint8)
    sticker_transparent = np.array(sticker_transparent, dtype=np.uint8)
    for row in range(rows):
        for col in range(cols):
            if sticker[row,col,0] > 240 and sticker[row,col,1] > 240 and sticker[row,col,2] > 240:
                sticker_ghost[row,col] = [0, 0, 0]
            else:
                sticker_ghost[row,col] = sticker[row,col]

            if sticker_ghost[row,col,0] <1 and sticker_ghost[row,col,1] <1 and sticker_ghost[row,col,2] <1:
                sticker_ghost[row,col] = [1, 1, 1]
            else:
                sticker_ghost[row,col] = [0, 0, 0]
            
            if sticker_ghost[row,col,0] == 0 and sticker_ghost[row,col,1] == 0 and sticker_ghost[row,col,2] == 0:
                sticker_transparent[row,col] = sticker[row,col]

    return sticker_ghost, sticker_transparent

image_tiger_ghost, image_tiger_transparent = transparent_sticker(image_tiger)

mamad_tiger_image = image_mamad*image_tiger_ghost + image_tiger_transparent

cv2.imwrite('output/image_tiger_transparent.jpg',image_tiger_transparent)
cv2.imwrite('output/image_tiger_ghost.jpg',image_tiger_ghost*255)
cv2.imwrite('output/mamad_tiger.jpg',mamad_tiger_image)
mamad_tiger_image = cv2.resize(mamad_tiger_image, [mamad_tiger_image.shape[0]//2, mamad_tiger_image.shape[1]//2])
cv2.imwrite('output\mamad_tiger_image_small.jpg',mamad_tiger_image)