from PIL import Image, ImageOps
import numpy as np


# Digital Image B&W, Grayscale Color Modes
# This method can be particularly useful if you’re looking to achieve a truly B&W or grayscale image.

# L : This image mode has one channel that can take any value between 0 and 255 representing white, black and all the
# shades of gray in between. It’s an 8-bit grayscale image mode. L stands for Luminance channel.

# LA : Represents L with Alpha transparency channel. This mode can be used to achieve grayscale images
# with transparency. And don’t forget only png and gif image file types support transparency channel.

# 1 : This image mode is true black & white. It only has one channel which takes only two value representing
# full white or full black. There is no in between meaning no gray.

img = Image.open("perfil-en-blanco-y-negro.jpg")
imgGray = img.convert('L')
imgGray.show()

# gray_image = ImageOps.grayscale(img)
# gray_image.show()

img_pixels = list(imgGray.getdata())
print(img_pixels)

lst = []
# la entrada es igual a la salida: P = Q
for i in img_pixels:
    lst.append(i)


new_img = Image.new('L', imgGray.size)
new_img.putdata(lst)
new_img.show()

