import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import convolve2d

input_image=plt.imread('E:\\COLLEGE 5TH SEM\\college\\6_class\\lamborghini.jpg')

if input_image.shape[-1]==3:
    input_image=np.mean(input_image,axis=-1)

laplacian_kernal=np.array([[0,1,0],[1,-4,1],[0,1,0]])

filtered_image=convolve2d(input_image,laplacian_kernal,mode='same',boundary='wrap')
filtered_image=np.clip(filtered_image,0,255)

plt.figure(figsize=(12,6))
plt.subplot(121)
plt.title("original image")
plt.imshow(input_image,cmap="gray")

plt.subplot(122)
plt.title("Filtered image")
plt.imshow(filtered_image,cmap="gray")
plt.show()


#rassa