from PIL import Image

# En esta operación tambien aplicamos 2 umbrales, umbral1= 40 y umbral2=190,
# con la diferencia que ahora las intensidades de pixeles que sean menor a 40 o mayor a 190
# se volverán 0(negro) y los que esten dentro del rango de los umbrales se volveran 25(blanco).

umbral1 = int(input("Umbral 1 es: \t"))
umbral2 = int(input("Umbral 2 es: \t"))

img = Image.open('perfil-en-blanco-y-negro.jpg')
img_gray = img.convert('L')
img_gray.show()

img_pixels = list(img_gray.getdata())
print(img_pixels)

lst = []

for i in img_pixels:
    # q =  0 para p <= p1, ó p >= p2
    if i <= umbral1 or i >= umbral2:
        lst.append(0)
    # q =  255 para p1, < p < p2
    else:
        lst.append(255)


img_new = Image.new('L', img_gray.size)
img_new.putdata(lst)
img_new.show()