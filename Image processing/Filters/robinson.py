# pip install scipy
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import convolve2d

input_image=plt.imread('E:\\COLLEGE 5TH SEM\\Image processing\\5_class\\lamborghini.jpg ')

#convert the image into gray scale
if input_image.shape[-1]==3:
    input_image=np.mean(input_image,axis=-1)

def robinson_operator(image):
    kernels=[
        np.array([[-1,-2,-1],[0,0,0],[1,2,1]]),
        np.array([[-2,-1,0],[-1,0,1],[0,1,2]]),
        np.array([[-1,0,1],[-2,0,2],[-1,0,1]]),
        np.array([[0,1,2],[-1,0,1],[-2,-1,0]])
        # np.array([[0,0,1],[2,1,-1],[-2,-1,0]]),
        # np.array([[0,1,2],[1,-1,-2],[-1,0,0]]),
        # np.array([[1,2,1],[-1,-2,-1],[0,0,0]]),
        # np.array([[2,1,-1],[-2,-1,0],[0,0,1]])
    ]
    gradient_magnitude=[convolve2d(image,kernel,mode='same',boundary='symm') for kernel in kernels]
    gradient_magnitude=np.max(gradient_magnitude,axis=0)
    return gradient_magnitude

filter_image=robinson_operator(input_image)


# display
plt.figure(figsize=(12,6))
plt.subplot(121)  # row col img
plt.title("original image")
plt.imshow(input_image,cmap="gray")

plt.subplot(122)
plt.title("Filterd image(robinson_filter)")
plt.imshow(filter_image,cmap="gray")

plt.show()