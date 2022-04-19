import cv2 as cv
import numpy as np

def change_brightness(img, c):
    for i in range(0, img.shape[0]):
        for j in range(0, img.shape[1]):
            if(c > 0):
                img[i][j][0] = img[i][j][0] + c if img[i][j][0] + c < 255 else 255
                img[i][j][1] = img[i][j][1] + c if img[i][j][1] + c < 255 else 255
                img[i][j][2] = img[i][j][2] + c if img[i][j][2] + c < 255 else 255
            else:
                img[i][j][0] = img[i][j][0] + c if img[i][j][0] + c > 0 else 0
                img[i][j][1] = img[i][j][1] + c if img[i][j][1] + c > 0 else 0
                img[i][j][2] = img[i][j][2] + c if img[i][j][2] + c > 0 else 0
    return img


path = "img.jfif"

img = cv.imread(path)

scale_percent = 30 # percent of original size
width = int(img.shape[1] * scale_percent / 100)
height = int(img.shape[0] * scale_percent / 100)
dim = (width, height)

# resize image
resized = cv.resize(img, dim)

cv.imshow("Demo", change_brightness(resized, 150))
cv.waitKey()