import sys
import cv2
import numpy as np

def change_brightness(img, alpha, beta):
    img_new = np.asarray(alpha*img + beta, dtype=int)   # cast pixel values to int
    img_new[img_new>255] = 255
    img_new[img_new<0] = 0
    return img_new

if __name__ == "__main__":
    alpha = 1.0
    beta = 90
    if len(sys.argv) == 3:
        alpha = float(sys.argv[1])
        beta = int(sys.argv[2])
    img = cv2.imread('img.jfif')       # [height, width, channel]
    
    # change image brightness g(x,y) = alpha*f(x,y) + beta
    img_new = change_brightness(img, alpha, beta)
    
    cv2.imwrite('img_3_new.jpg', img_new)
    img_new = cv2.imread('img_3_new.jpg')
    cv2.imshow("img_3",img) 
    cv2.imshow("img_3_new",img_new)
    cv2.waitKey()



# import sys
# import cv2
# import numpy as np


# def change_brightness(img, alpha, beta):
#     img_new = np.asarray(1.0 * img + beta, dtype=int)  # cast pixel values to int
#     img_new[img_new > 255] = 255
#     img_new[img_new < 0] = 0
#     return img_new




# alpha = 1.0
# beta = 150
# if len(sys.argv) == 3:
#     alpha = float(sys.argv[1])
#     beta = int(sys.argv[2])
# img = cv2.imread('img_3.jpg')  # [height, width, channel]
# cv2.imshow("img_3",img)
# # change image brightness g(x,y) = alpha*f(x,y) + beta
# img_new = change_brightness(img, alpha, beta)

# cv2.imwrite('img_3_new.jpg', img_new)
# img_new = cv2.imread('img_3_new.jpg')
# cv2.imshow("img_3_new",img_new)
# cv2.waitKey()



# import cv2 as cv
# import numpy as np

# def change_brightness(img, c):
#     for i in range(0, img.shape[0]):
#         for j in range(0, img.shape[1]):
#             if(c > 0):
#                 img[i][j][0] = img[i][j][0] + c if img[i][j][0] + c < 255 else 255
#                 img[i][j][1] = img[i][j][1] + c if img[i][j][1] + c < 255 else 255
#                 img[i][j][2] = img[i][j][2] + c if img[i][j][2] + c < 255 else 255
#             else:
#                 img[i][j][0] = img[i][j][0] + c if img[i][j][0] + c > 0 else 0
#                 img[i][j][1] = img[i][j][1] + c if img[i][j][1] + c > 0 else 0
#                 img[i][j][2] = img[i][j][2] + c if img[i][j][2] + c > 0 else 0
#     return img


# path = "img.jfif"

# img = cv.imread(path)

# scale_percent = 80 # percent of original size
# width = int(img.shape[1] * scale_percent / 100)
# height = int(img.shape[0] * scale_percent / 100)
# dim = (width, height)

# # resize image
# resized = cv.resize(img, dim)

# cv.imshow("Demo_1",img)
# cv.imshow("Demo_2", change_brightness(resized, 50))
# cv.waitKey()