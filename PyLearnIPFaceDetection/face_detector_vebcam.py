import cv2
import numpy as np

def chess_face(image):
    faces = face_datector.detectMultiScale(image)
    for face in faces:
        x, y, w, h = face
        face_image = image[y:y+h, x:x+w]
        face_image_small = cv2.resize(face_image, [10, 10])
        face_image_big = cv2.resize(face_image_small, [w, h], interpolation=cv2.INTER_NEAREST)
        image[y:y+h, x:x+w] = face_image_big

    return image

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
    faces = face_datector.detectMultiScale(image_gary,1.3)
    for face in faces:
        x, y, w, h = face
        sticker_ghost = cv2.resize(sticker_ghost, [w, h])
        sticker_transparent = cv2.resize(sticker_transparent, [w, h])
        image[y:y+h, x:x+w] = sticker_ghost*image[y:y+h, x:x+w] + sticker_transparent

    return image

def eye_smile(image, sticker_ghost, sticker_transparent, smile_ghost, smile_transparent, eye_datector, smaile_datector):
    image_gary = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    eyes = eye_datector.detectMultiScale(image_gary,1.1)
    smiles = smaile_datector.detectMultiScale(image_gary,1.3)
    if len(eyes) == 2:
        eye_x_min = np.minimum(eyes[0,0], eyes[1,0])
        eye_x_max = np.maximum(eyes[0,0], eyes[1,0]) + eyes[1,2]
        eye_y_min = np.minimum(eyes[0,1], eyes[1,1])
        eye_y_max = np.maximum(eyes[0,1], eyes[1,1]) + eyes[1,3]
        sticker_ghost = cv2.resize(sticker_ghost, [eye_x_max - eye_x_min, eye_y_max - eye_y_min])
        sticker_transparent = cv2.resize(sticker_transparent, [eye_x_max - eye_x_min, eye_y_max - eye_y_min])
        image[eye_y_min:eye_y_max, eye_x_min:eye_x_max] = sticker_ghost*image[eye_y_min:eye_y_max, eye_x_min:eye_x_max]//2 + sticker_transparent//2 + image[eye_y_min:eye_y_max, eye_x_min:eye_x_max]//2
    
        for smile in smiles:
            x, y, w, h = smile
            if y > eye_y_max and eye_x_min < x < eye_x_max and (x+w) < eye_x_max and y < (eye_y_max + (eye_x_max - eye_x_min)*.5):
                smile_ghost = cv2.resize(smile_ghost, [w, h])
                smile_transparent = cv2.resize(smile_transparent, [w, h])
                image[y:y+h, x:x+w] = smile_ghost*image[y:y+h, x:x+w] + smile_transparent
            # break

    return image

def mirror(image):
    x_size = image.shape[1]
    flipVertical = cv2.flip(image[:,:x_size//2], 1)
    image[:,x_size//2:] = flipVertical

    return image


image_sticker_emoji = cv2.imread('media\emoji4.png')
image_sticker_emoji = cv2.resize(image_sticker_emoji, (image_sticker_emoji.shape[0]//8,image_sticker_emoji.shape[1]//6))
image_sticker_emoji_ghost, image_sticker_emoji_transparent = transparent_sticker(image_sticker_emoji)

image_glass = cv2.imread('media\glass5.jpg')
image_glass_ghost, image_glass_transparent = transparent_sticker(image_glass)

image_smile = cv2.imread('media\smile3.jpg')
# image_smile = cv2.resize(image_smile, (image_smile.shape[0]//20,image_smile.shape[1]//20))
image_smile_ghost, image_smile_transparent = transparent_sticker(image_smile)

face_datector = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_datector = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye_tree_eyeglasses.xml')
smaile_datector = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_smile.xml')

cap = cv2.VideoCapture(0)
_, frame = cap.read()
rows, cols, _ = frame.shape
writer = cv2.VideoWriter('media\mamad.mp4', cv2.VideoWriter_fourcc(*'MJPG'), 8, (cols, rows))

choice = 1

while True:
    _, frame = cap.read()
    frame = cv2.flip(frame, 1)

    if choice == 1:
        frame = chess_face(frame)
    elif choice == 2:
        frame = sticker_face(frame, image_sticker_emoji_ghost, image_sticker_emoji_transparent, face_datector)
    elif choice == 3:
        frame = eye_smile(frame, image_glass_ghost, image_glass_transparent,
        image_smile_ghost, image_smile_transparent, eye_datector, smaile_datector)
    elif choice == 4:
        frame = mirror(frame)

    writer.write(frame)
    cv2.imshow('mamad',frame)
    choice1 = cv2.waitKey(5)
    if choice1 & 0xFF == ord('q'):
        break
    elif choice1 & 0xFF == ord('1'):
        choice = 1
    elif choice1 & 0xFF == ord('2'):
        choice = 2
    elif choice1 & 0xFF == ord('3'):
        choice = 3
    elif choice1 & 0xFF == ord('4'):
        choice = 4

writer.release()
cap.release()
cv2.destroyAllWindows()


