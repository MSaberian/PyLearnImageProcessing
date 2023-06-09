import statistics
from PIL import ImageFont, ImageDraw, Image  
import numpy as np
import matplotlib.pyplot as plt
import cv2

def encrypting(image):
    image = image.astype(float)
    key = np.random.normal(0, 0.1, (image.shape[0], image.shape[1], 3)) + np.finfo(float).eps
    image_encrypted = (image / key).astype(int) 
    
    return key, image_encrypted

def decryption(image, key):
    image_Decryption = image.astype(float)*key
    image_Decryption = image_Decryption.astype(int)

    return image_Decryption
