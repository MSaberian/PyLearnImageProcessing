import random
import numpy as np
import cv2

def transparent_sticker(sticker):
    rows, cols, _ = sticker.shape
    sticker_ghost = np.zeros(sticker.shape)
    sticker_transparent = np.zeros(sticker.shape)
    sticker_ghost = np.array(sticker_ghost, dtype=np.uint8)
    sticker_transparent = np.array(sticker_transparent, dtype=np.uint8)
    for row in range(rows):
        for col in range(cols):
            if sticker[row,col,0] == 255 and sticker[row,col,1] == 255 and sticker[row,col,2] == 255:
                sticker_ghost[row,col] = [0, 0, 0]
            else:
                sticker_ghost[row,col] = sticker[row,col]

            if sticker_ghost[row,col,0] <10 and sticker_ghost[row,col,1] <10 and sticker_ghost[row,col,2] <10:
                sticker_ghost[row,col] = [1, 1, 1]
            else:
                sticker_ghost[row,col] = [0, 0, 0]
            
            if sticker_ghost[row,col,0] == 0 and sticker_ghost[row,col,1] == 0 and sticker_ghost[row,col,2] == 0:
                sticker_transparent[row,col] = sticker[row,col]
        if sticker.shape == (220, 400, 3):
            sticker_ghost[50:150,150:200] = [0, 0, 0]
            sticker_transparent[50:150,150:200] = sticker[50:150,150:200]

    return sticker_ghost, sticker_transparent

def sticker_face(image, sticker_ghost, sticker_transparent, face_datector):
    image_gary = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    faces = face_datector.detectMultiScale(image_gary,7)
    for face in faces:
        x, y, w, h = face
        # face_image = image[y:y+h, x:x+w]
        sticker_ghost = cv2.resize(sticker_ghost, [w, h])
        sticker_transparent = cv2.resize(sticker_transparent, [w, h])
        image[y:y+h, x:x+w] = sticker_ghost*image[y:y+h, x:x+w] + sticker_transparent

    return image

    
image = cv2.imread('media\Big_bang.jpg')
# image_gary = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

image_sticker_emoji = cv2.imread('media\smile.jpg')
image_sticker_emoji = cv2.resize(image_sticker_emoji, (image_sticker_emoji.shape[1]//20,image_sticker_emoji.shape[0]//20))

image_sticker_emoji_ghost, image_sticker_emoji_transparent = transparent_sticker(image_sticker_emoji)

cv2.imshow('image_sticker_emoji',image_sticker_emoji)
cv2.imshow('image_sticker_emoji_ghost',image_sticker_emoji_ghost*255)
cv2.imshow('image_sticker_emoji_transparent',image_sticker_emoji_transparent)

# face_datector = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_smile.xml')

# image = sticker_face(image, image_sticker_emoji_ghost, image_sticker_emoji_transparent, face_datector)
        
# cv2.imshow('image_gary',image)
# cv2.imwrite('media\Batman.jpg',image_bat)
cv2.waitKey()


