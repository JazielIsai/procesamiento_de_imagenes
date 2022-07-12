# library
import numpy as np
import cv2

img = cv2.imread('perfil-en-blanco-y-negro.jpg', 0) # load img

print(img)



cv2.imshow("image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()


cv2.imwrite('perfil-en-blanco-y-negro_copy.png', img)