import matplotlib.pyplot as plt
import numpy as np

img=plt.imread('E:\\COLLEGE 5TH SEM\\college\\prac7_class\\high.jpeg')

def grayscale(img):
    height,width=img.shape[:2]  #convert into two dimension
    grayimg=np.zeros((height,width),dtype=np.uint8)# making container

    for i in range(height):
        for j in range(width):
            red=img[i,j,0]
            green=img[i,j,1]
            blue=img[i,j,2]
            gray_value=0.28*red+0.59*green+0.11*blue
            grayimg[i,j]=gray_value
    return grayimg

gray=grayscale(img)

def negativeimg(gray):
    height,width=img.shape[:2]  #convert into two dimension
    negimg=np.zeros((height,width),dtype=np.uint8)# making container

    for i in range(height):
        for j in range(width):
            red=img[i,j,0]
            green=img[i,j,1]
            blue=img[i,j,2]
            neg_value=255-(0.28*red+0.59*green+0.11*blue)
            negimg[i,j]=neg_value
    return negimg

neg=negativeimg(gray)
print(gray.shape)

plt.figure(figsize=(12,6))
plt.subplot(131)
plt.title('original image')
plt.imshow(img)


plt.subplot(132)
plt.title('gray image')
plt.imshow(gray, cmap='gray')

plt.subplot(133)
plt.title('negative image')
plt.imshow(neg,cmap='gray')
plt.show()