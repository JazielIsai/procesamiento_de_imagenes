from PIL import Image

# En esta operación lo que se busca es reducir los niveles grises que tiene una imagen,
# como sabemos inicialmente tenemos 256 niveles de gris (0-255), e
# ntonces esta operación nos permite definir
# que cantidad de niveles de gris queremos tener en nuestra imagen resultante.
#
# 10.- Operador reducción nivel gris
#
#     q = 0 para p <= p1
#     -q1 = para p1 < p <= p2
#     q2 = para p2 < p <= p3
#     .
#     .
#     qn para pn-1 < p <= 255

img = Image.open('perfil-en-blanco-y-negro.jpg')
img_gray = img.convert('L')
img_gray.show()

img_pixels = list(img_gray.getdata())
print(img_pixels)

lst = []



