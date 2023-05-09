import cv2
import numpy as np

my_image = cv2.imread('C:/Users/slgzo/OneDrive/Resimler/Ayrton Senna.jpg')

blue, green, red = cv2.split(my_image)

green.fill(0)

red = np.clip(red + 50, 0, 255)
blue = np.clip(blue + 50, 0, 255)

modified_img = cv2.merge((blue, green, red))

cv2.imshow('Modified New Image', modified_img)
cv2.waitKey(0)

original_img = cv2.merge((blue, green, red))

cv2.imshow('Your Original Image', original_img)
cv2.waitKey(0)
