from PIL import Image
import numpy as np

# El operador Umbral nos permite establecer un límite(umbral) el cual establecerá que todas las intensidades
# de pixeles menores a ese umbral se conviertan en 0(negro) y las intensidades mayores a ese umbral
# se convertiran en 255(blanco).

umbral = int(input("El umbral es de: \t"))

img = Image.open('perfil-en-blanco-y-negro.jpg')
img_gray = img.convert('L')
img_gray.show()

img_pixels = list(img_gray.getdata())
print(img_pixels)

lst = []

for i in img_pixels:
    # q = 0 para p <= p
    if i < umbral:
        lst.append(0)
    # q = 255 para p > p
    else:
        lst.append(255)

img_new = Image.new('L', img_gray.size)
img_new.putdata(lst)
img_new.show()