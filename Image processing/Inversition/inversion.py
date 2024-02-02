# pip install opencv-python pillow matplotlib

from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

path="E:\\COLLEGE 5TH SEM\\college\\2_class\\imag.jpg"

im=Image.open(path)
arr=np.array(im)
print(arr)
im=im.convert("L")
plt.imshow(im,cmap='gray')
plt.show()

width,height=im.size()

inverted=np.zeros((width),(height))

for i in range(width):
    for j in range (height):
        pixel=im.getpixel((i,j))

        inverted[i,j]=255-pixel

inverted=inverted.T
inverted=Image.fromarray(inverted.astype('unit8'))
inverted.show()
plt.imshow(im,cmap='gray')
plt.show()
plt.imshow(inverted,cmap='gray')
plt.show()