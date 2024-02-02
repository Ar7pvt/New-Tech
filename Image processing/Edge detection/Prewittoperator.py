import numpy as np
import matplotlib.pyplot as plt

from scipy.signal import convolve2d

image=plt.imread('E:\\COLLEGE 5TH SEM\\college\\5_class\\lamborghini.jpg ')

#convert the image into gray scale
if image.shape[-1]==3:
    image=np.mean(image,axis=-1)

# prewitt operator
def prewitt(image):
    prewitt_kernel_x = np.array([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]])
    prewitt_kernel_y = np.array([[-1, -1, -1], [0, 0, 0], [1, 1, 1]])

    edges_x = convolve2d(image,prewitt_kernel_x,mode='same',boundary='symm')
    edges_y = convolve2d(image,prewitt_kernel_y,mode='same',boundary='symm')

    edge_image = np.sqrt(edges_x**2 + edges_y**2)
    return edge_image

prewitt_image=prewitt(image)

plt.figure(figsize=(12,6))
plt.subplot(121)
plt.title('Gray image')
plt.imshow(image,cmap='gray')

plt.subplot(122)
plt.title('Prewitt image')
plt.imshow(prewitt_image, cmap='gray')


plt.show()