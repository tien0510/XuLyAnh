import cv2 as cv
import numpy as np

arr = []
arr2 = []
arr3= []
L = 100
for i in range(0,256):
    arr.append(0)
    arr2.append(0)
    arr3.append(0)

def b1(img):
    for i in range(0, img.shape[0]):
        for j in range(0, img.shape[1]):
            arr[img[i][j]] = arr[img[i][j]] + 1


def b2():
    for i in range(0, 256):
        if(i == 0):
            arr2[0] = arr[0]
        else:
            arr2[i] = arr2[i-1] + arr[i]

def b3(img):
    for i in range(0, 256):
        if (i == 0):
            arr3[0] = 0
        else:
            arr3[i] = round(((arr2[i] - arr2[0])/ ( img.shape[0] * img.shape[1] )) * (L - 1))

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

img = cv.imread(path,0)

scale_percent = 30  # percent of original size
width = int(img.shape[1] * scale_percent / 100)
height = int(img.shape[0] * scale_percent / 100)
dim = (width, height)
resized = cv.resize(img, dim)

b1(img)
b2()
b3(img)
print(arr)
print(arr2)
print(arr3)

cv.imshow("After", change_brightness(resized, 150))
cv.waitKey()
