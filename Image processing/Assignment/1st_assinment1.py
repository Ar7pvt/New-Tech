# Q1. Write a program using Python:
# i) Conversion of the color image (RGB) to gray image. (Use ratios 0.3:0.58:0.11)
# ii) Inversion of color to form negative of converted grayscale image.

import matplotlib.pyplot as plt
import numpy as np

img=plt.imread('E:\\COLLEGE 5TH SEM\\college\\7prac_class\\high.jpeg')

def grayscale(img):
    height,width=img.shape[:2]  #convert into two dimension
    grayimg=np.zeros((height,width),dtype=np.uint8)# making container

    for i in range(height):
        for j in range(width):
            red=img[i,j,0]
            green=img[i,j,1]
            blue=img[i,j,2]
            gray_value=0.3*red+0.58*green+0.11*blue
            grayimg[i,j]=gray_value
    return grayimg

gray=grayscale(img)

def negativeimg(gray):
    height,width=img.shape[:2]  #convert into two dimension
    negimg=np.zeros((height,width),dtype=np.uint8)# making container

    negimg=255-gray
    return negimg

neg=negativeimg(gray) 

# Plotting a figure of width 12 and height 6
plt.figure(figsize=(12,6))
plt.subplot(131) #row, col, no
plt.title('original image')
plt.imshow(img)


plt.subplot(132)
plt.title('gray image')
plt.imshow(gray, cmap='gray')

plt.subplot(133)
plt.title('negative image')
plt.imshow(neg,cmap='gray')
plt.show()