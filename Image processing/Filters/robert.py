# pip install scipy
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import convolve2d

input_image=plt.imread('E:\\COLLEGE 5TH SEM\\Image processing\\5_class\\lamborghini.jpg ')

#convert the image into gray scale
if input_image.shape[-1]==3:
    input_image=np.mean(input_image,axis=-1)

def robert_operator(image):
    kernal_x = np.array([[1,0],[0,-1]])
    kernal_y = np.array([[0,1],[-1,0]])
    gradient_x=convolve2d(image,kernal_x,mode='same',boundary='symm')
    gradient_y=convolve2d(image,kernal_y,mode='same',boundary='symm')
    gradient_magnitude=np.sqrt(gradient_x**2+gradient_y**2)
    return gradient_magnitude


filter_image=robert_operator(input_image)


# display
plt.figure(figsize=(12,6))
plt.subplot(121)  # row col img
plt.title("original image")
plt.imshow(input_image,cmap="gray")

plt.subplot(122)
plt.title(f"Filterd image")
plt.imshow(filter_image,cmap="gray")

plt.show()