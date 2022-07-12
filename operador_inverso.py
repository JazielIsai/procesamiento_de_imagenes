from PIL import Image
import numpy as np

img = Image.open("perfil-en-blanco-y-negro.jpg")
img_gray = img.convert('L')
img_gray.show()

img_pixels = list(img_gray.getdata())
print(img_pixels)

lst = []
for i in img_pixels:
    # la salida es igual a a la entrada: Q = P EJEMPLO: Q = 255 - P  = 0
    if i < 150:
       lst.append(255)
    else:
        lst.append(0)

new_img = Image.new('L', img_gray.size)
new_img.putdata(lst)
new_img.show()