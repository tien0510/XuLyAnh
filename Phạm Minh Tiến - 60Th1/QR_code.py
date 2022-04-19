import cv2
import numpy as np

image = cv2.imread('qr_tien.jpg')

scale_percent = 50  # 50%
width = int(image.shape[1] * scale_percent / 100)
height = int(image.shape[0] * scale_percent / 100)
dim = (width, height)
image = cv2.resize(image, dim)

original = image.copy()

imageGray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

imageBlur = cv2.GaussianBlur(imageGray, (9,9), 0)
#phân ngưỡng 
imageThresh = cv2.threshold(imageBlur, 0, 255, cv2.. + cv2.THRESH_OTSU)[1]
cv2.imshow('imageThresh', imageThresh)


kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (10,10))
# lấp đầy khoảng trống
fill = cv2.morphologyEx(imageThresh, cv2.MORPH_CLOSE, kernel, iterations=2)
cv2.imshow('fill', fill)

# truy xuất đường bao ngoài cùng,nén đoạn ngang dọc để lại điểm cuối
contours = cv2.findContours(fill, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
contours = contours[0] if len(contours) == 2 else contours[1]

# exit()
for c in contours:
    peri = cv2.arcLength(c, True)
    approx = cv2.approxPolyDP(c, 0.04 * peri, True)

    # tọa độ điểm đầu,chiều rộng w, chiều cao h 
    x,y,w,h = cv2.boundingRect(approx)
    area = cv2.contourArea(c)
    ar = w / float(h)

    if len(approx) == 4 and area > 1000 and (ar > .85 and ar < 1.3):

        cv2.rectangle(image, (x, y), (x + w, y + h), (36,255,12), 3)

        LAST = original[y:y+h, x:x+w]
        cv2.imwrite('LAST.png', LAST)
cv2.imshow('image', image)
cv2.imshow('LAST', LAST)
cv2.waitKey()