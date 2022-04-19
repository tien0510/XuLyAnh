import cv2 as cv
import numpy as np

def medium(matrix, n):
    sum = 0
    for row in matrix:
        for element in row:
            sum += element
    return round(sum/n)

def normalizedBoxFilter(img, x, y):
    x1 = x//2
    y1 = y//2
    width = img.shape[1] 
    height = img.shape[0]
    copy_img = np.copy(img)
    for i in range(height):
        for j in range(width):
            height1 = i - x1        if i        > x1      else 0
            height2 = i + x1 + 1    if i + x1   < height  else height
            width1  = j - y1        if j        > y1      else 0
            width2  = j + y1 + 1    if j + y1   < width   else width
            # print(height1, height2, width1, width2)
            matrix = copy_img[height1:height2, width1:width2]
            # print(matrix, "\n")
            img[i][j] = medium(matrix, x*y)

path = "img.jfif"

x = int(input("Nhap chieu dai mat na: "))
y = int(input("Nhap chieu rong mat na: "))


# img = np.array([[131, 137, 141],
#         [139, 133, 133],
#         [138, 132, 127]])

img = cv.imread(path, 0)

print(img)
cv.imshow("Truoc khi khu nhieu", img)


normalizedBoxFilter(img, x, y)

print(img)
cv.imshow("Sau khi loc trung binh", img)

cv.waitKey()
