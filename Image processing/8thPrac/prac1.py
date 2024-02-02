# add noise then
# a median filter
#b gaussian filter

import matplotlib.pyplot as plt
import numpy as np
import random

image=plt.imread('E:\\COLLEGE 5TH SEM\\college\\7prac_class\\high.jpeg')

# for grey scale

def greyscale(image):
    height,width=image.shape[:2]
    greyimage=np.zeros((height,width),dtype=np.uint8)

    for i in range(height):
        for j in range(width):
            red=image[i,j,0]
            green=image[i,j,1]
            blue=image[i,j,2]
            greyimage[i,j]=0.3*red+0.58*green+0.11*blue
    return greyimage

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

grey=greyscale(image)
imageWithNoise=saltpepper(grey, 0.1)

plt.imshow(grey,cmap='gray')
plt.show()

plt.imshow(imageWithNoise,cmap='gray')
plt.show()
