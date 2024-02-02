# Q2. Given an image, perform the following operations to it:
# i. Add salt-pepper noise to it.
# ii. Perform median filter to it.
# iii. Perform Gaussian filter to it.

import numpy as np
import matplotlib.pyplot as plt
import random
import cv2
from scipy.signal import convolve2d


def saltpepper(image,density):
    output=np.zeros(image.shape,np.uint8)
    threshold=1-density

    for i in range(image.shape[0]):
        for j in range (image.shape[1]):
            possibility=random.random()
            if(possibility<density):
                output[i][j]=0
            elif(possibility>threshold):
                output[i][j]=255
            else:
                output[i][j]=image[i][j]
    return output

def MedianFilter(image, filter_size):
     height, width = image.shape[:2]
     #create an empty array with same szie as input image
     output = np.zeros((height, width), np.uint8)

     #create the kernelarray of filter as same size as filter size
     filter_array = [image[0][0]]*filter_size  # making empty array of size [0,0,0,0,0,0,0,0,0]

     #deal with filter size = 3x3
     if filter_size ==9:
          for j in range(1, image.shape[0]-1):
               for i in range(1, image.shape[1]-1):
                    filter_array[0] = image[j-1, i-1]
                    filter_array[1] = image[j, i-1]
                    filter_array[2] = image[j+1, i-1]
                    filter_array[3] = image[j-1, i]
                    filter_array[4] = image[j, i]
                    filter_array[5] = image[j+1, i]
                    filter_array[6] = image[j-1, i+1]
                    filter_array[7] = image[j, i+1]
                    filter_array[8] = image[j+1, i+1]
                    #sort the array
                    filter_array.sort()
                    #nput the medium into ouput array
                    output[j][i] = filter_array[4]
     return output                




# image=plt.imread("E:\\COLLEGE 5TH SEM\\college\\6_class\\lamborghini.jpg")
image = cv2.cvtColor(cv2.imread('E:\\COLLEGE 5TH SEM\\college\\6_class\\lamborghini.jpg'), cv2.COLOR_BGR2GRAY)


def gaussian_kernel(size, sigma):
    kernel= np.fromfunction(
        lambda x, y: (1/ (2*np.pi*sigma*2))*np.exp(-((x-(size-1)/2)**2 + (y-(size-1)/2)**2)/(2*sigma*2)),(size,size)
    )
    return kernel / np.sum(kernel)


#generate the gaussian kernal
gaussian_filter_kernel= gaussian_kernel(11, 3.5)

#applying gaussian filter convulation
filter_image=convolve2d(image,gaussian_filter_kernel,mode='same',boundary='symm')


imageWithNoise=saltpepper(image, 0.1)

median = MedianFilter(imageWithNoise, 9)

plt.figure(figsize=(18,9))
plt.subplot(141)
plt.title('Gray image')
plt.imshow(image,cmap='gray')

plt.subplot(142)
plt.title('Saltpeper image')
plt.imshow(imageWithNoise, cmap='gray')

plt.subplot(143)
plt.title('Median image')
plt.imshow(median, cmap='gray')

plt.subplot(144)
plt.title('gaussian image')
plt.imshow(filter_image, cmap='gray')


plt.show()