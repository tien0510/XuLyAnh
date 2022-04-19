import cv2 as cv
import numpy as np
import statistics

# đọc ảnh
path = "img.jfif"

img = cv.imread(path, 0)
print(img)
img2 = img

width = int(img.shape[1])
height = int(img.shape[0])

width_boloc = int(input("Chiều rộng bộ lọc trung vị : "))
height_boloc = int(input("Chiều cao bộ lọc trung vị : "))

size = width_boloc * height_boloc
width_boloc1_2 = (width_boloc - 1) // 2
height_boloc1_2 = (height_boloc - 1) // 2

for i in range(0,height):
    for j in range(0, width):
        trungvi = []
        for k in range(i - height_boloc1_2, i + height_boloc1_2 + 1 ):
            for t in range(j - width_boloc1_2, j + width_boloc1_2 + 1):

                if (k >= 0 and t >= 0) and (k < height and t < width ) :
                    trungvi.append(img[k][t])
        trungvi.sort()

        img2[i][j] =  trungvi[len(trungvi)//2]
print(img2)
cv.imshow("Sau khi loc trung vi", img2)
cv.waitKey()
