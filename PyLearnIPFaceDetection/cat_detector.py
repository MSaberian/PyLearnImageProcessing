import cv2

cat_datector = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalcatface_extended.xml')

for i in range(5):
    
    image_cat = cv2.imread(f'input\cat{i}.jpg')
    image_cat = cv2.cvtColor(image_cat,cv2.COLOR_BGR2GRAY)
    cat_faces = cat_datector.detectMultiScale(image_cat)
    print(f'Cats number in cat{i} image is: {len(cat_faces)}')
