import cv2 as cv
import numpy as np

def medium(height,width,height_2,width_2,img,image):
    for i in range(0,height):
        for j in range(0, width):
            total = 0

            for m in range(i - height_2, i + height_2 + 1 ):
                for n in range(j - width_2, j + width_2 + 1):

                    if (m >= 0 and n >= 0) and (m < height and n < width ) :
                        total = total + img[m][n]
            tb = round(total/size)
            image[i][j] = tb
    return image
path = "img.jfif"
img = cv.imread(path, 0)

image = img
width = int(img.shape[1])
height = int(img.shape[0])
width_1  = int(input("Nhập chiều rộng : "))
height_1 = int(input("Nhập chiều cao  : "))
cv.imshow("Sau truoc loc trung binh", img)

size = width_1 * height_1
width_2 = (width_1 - 1) // 2
height_2 = (height_1 - 1) // 2
# tiến hành lọc trung bình
medium(height,width,height_2,width_2,img,image)

print(image)
cv.imshow("Sau khi loc trung binh", image)
cv.waitKey()

