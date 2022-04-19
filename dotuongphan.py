from PIL import Image, ImageEnhance
img = Image.open("img_3.jpg")
enhancer = ImageEnhance.Contrast(img)
for i in range(1, 3):
    factor = i / 4.0
    new_img = enhancer.enhance(factor)
    new_img.show()