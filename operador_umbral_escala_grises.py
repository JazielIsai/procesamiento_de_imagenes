from PIL import Image

# En esta operación aplicamos 2 umbrales, umbral1= 10 y umbral2=100,
# para que los pixeles que sean menor a 10 o mayor a 100 se volverán 255(blanco)
# y los que esten dentro del rango de los umbrales se quedarán con la misma intensidad
# en la que se encuentran en la imagen original.

umbral1 = int(input("Umbral 1 es: \t"))
umbral2 = int(input("Umbral 2 es: \t"))

img = Image.open('perfil-en-blanco-y-negro.jpg')
img_gray = img.convert('L')
img_gray.show()

img_pixels = list(img_gray.getdata())
print(img_pixels)

lst = []

for i in img_pixels:
    # q = 255 para p <= p1 ó p >= p2
    if i <= umbral1 or i >= umbral2:
        lst.append(255)
    # q = p para p1 < p < p2
    else:
        lst.append(i)

img_new = Image.new('L', img_gray.size)
img_new.putdata(lst)
img_new.show()