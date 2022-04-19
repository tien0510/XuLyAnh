import cv2 as cv
import numpy as np

arr = []

for i in range(0,256):
    arr.append(0)
def his(img):
    for i in range(0, img.shape[0]):
        for j in range(0, img.shape[1]):
            arr[img[i][j]] = arr[img[i][j]] + 1
    print(arr)

path = "img_3.jpg"

img = cv.imread(path, 0)

scale_percent = 30  # percent of original size
width = int(img.shape[1] * scale_percent / 100)
height = int(img.shape[0] * scale_percent / 100)
dim = (width, height)
resized = cv.resize(img, dim)

his(img)

# cv.imshow("Demo", change_brightness(resized, 150))
# cv.waitKey()