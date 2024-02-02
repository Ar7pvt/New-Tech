# Q1. Given a gray value image and write the program of the following tasks:
# Using different masks find the edges of the image:
# a) Robert’s operator,
# b) Laplacian operator,
# c) Prewitt operator.

import numpy as np
import matplotlib.pyplot as plt

from scipy.signal import convolve2d

image=plt.imread('E:\\COLLEGE 5TH SEM\\college\\5_class\\lamborghini.jpg ')

#convert the image into gray scale
if image.shape[-1]==3:
    image=np.mean(image,axis=-1)

# robert operator
def robert_operator(image):
    kernal_x = np.array([[1,0],[0,-1]])
    kernal_y = np.array([[0,1],[-1,0]])
    gradient_x=convolve2d(image,kernal_x,mode='same',boundary='symm')
    gradient_y=convolve2d(image,kernal_y,mode='same',boundary='symm')
    gradient_magnitude=np.sqrt(gradient_x**2+gradient_y**2)
    return gradient_magnitude

filter_image=robert_operator(image)

# laplacian filter
laplacian_kernal=np.array([[0,1,0],[1,-4,1],[0,1,0]])

filtered_image=convolve2d(image,laplacian_kernal,mode='same',boundary='wrap')
laplacianfil=np.clip(filtered_image,0,255)

# prewitt operator ar7
def prewitt(image):
    prewitt_kernel_x = np.array([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]])
    prewitt_kernel_y = np.array([[-1, -1, -1], [0, 0, 0], [1, 1, 1]])

    edges_x = convolve2d(image,prewitt_kernel_x,mode='same',boundary='symm')
    edges_y = convolve2d(image,prewitt_kernel_y,mode='same',boundary='symm')

    edge_image = np.sqrt(edges_x**2 + edges_y**2)
    return edge_image

prewitt_image=prewitt(image)

plt.figure(figsize=(12,6))
plt.subplot(141)
plt.title('Gray image')
plt.imshow(image,cmap='gray')

plt.subplot(142)
plt.title('robert ')
plt.imshow(filter_image, cmap='gray')

plt.subplot(143)
plt.title('laplacian image')
plt.imshow(laplacianfil, cmap='gray')

plt.subplot(144)
plt.title('Prewitt image')
plt.imshow(prewitt_image, cmap='gray')


plt.show()