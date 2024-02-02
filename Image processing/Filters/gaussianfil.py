# pip install scipy
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import convolve2d

input_image=plt.imread('E:\\COLLEGE 5TH SEM\\college\\5_class\\lamborghini.jpg ')
#convert the image into gray scale
if input_image.shape[-1]==3:
    input_image=np.mean(input_image,axis=-1)

#input filter size and sigma
filter_size=int(input("Enter filter size (odd integer): "))
sigma=float(input("Enter sigma (eg 1.5)"))
# Ensure filter size is odd
if filter_size%2==0:
    filter_size+=1

#create gaussian filter
def gaussian_kernel(size, sigma):
    kernel= np.fromfunction(
        lambda x, y: (1/ (2*np.pi*sigma*2))*np.exp(-((x-(size-1)/2)**2 + (y-(size-1)/2)**2)/(2*sigma*2)),(size,size)
    )
    return kernel / np.sum(kernel)


#generate the gaussian kernal
gaussian_filter_kernel= gaussian_kernel(filter_size, sigma)
#applying gaussian filter convulation
filter_image=convolve2d(input_image,gaussian_filter_kernel,mode='same',boundary='symm')

# display
plt.figure(figsize=(12,6))
plt.subplot(121)  # row col img
plt.title("original image")
plt.imshow(input_image,cmap="gray")

plt.subplot(122)
plt.title(f"Filterd image(Gaussian,sigma={sigma})")
plt.imshow(filter_image,cmap="gray")

plt.show()