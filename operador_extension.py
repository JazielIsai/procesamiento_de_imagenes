from PIL import Image

# Para este tipo de operador tambien se utilizan 2 umbrales,
# y se trabaja de la misma forma que en el operador umbral binario invertido,
# es decir suprimir todos los pixeles que se encuentren fuera del rango de los umbrales,
# la diferencia que cuando las intensidades de los pixeles se encuentran dentro de los umbrales
# entonces se aplica la siguiente función:
# (p-u1)*255/u2-u1
#
# En donde p es el valor de la intensidad del pixel inicial, u1 y u2 son los umbrales.

umbral1 = int(input("Umbral 1 es: \t"))
umbral2 = int(input("Umbral 2 es: \t"))

img = Image.open('perfil-en-blanco-y-negro.jpg')
img_gray = img.convert('L')
img_gray.show()

img_pixels = list(img_gray.getdata())
print(img_pixels)

lst = []

for i in img_pixels:
    # q  = 0  para p <= p1 ó p >= p2
    if i <= umbral1 or i >= umbral2:
        lst.append(0)
    # (p - p1) 255 / p2 - p1 para p1 < p < p2
    else:
        res = (i - umbral1) * 255 / umbral2 - umbral1
        lst.append(res)

img_new = Image.new('L', img_gray.size)
img_new.putdata(lst)
img_new.show()