# def negativeimg(gray):  vertexai 
#     height,width=img.shape[:2]  #convert into two dimension
#     negimg=np.zeros((height,width),dtype=np.uint8)# making container

#     for i in range(height):
#         for j in range(width):
#             red=img[i,j,0]
#             green=img[i,j,1]
#             blue=img[i,j,2]
#             neg_value=255-(0.28*red+0.59*green+0.11*blue)
#             negimg[i,j]=neg_value
#     return negimg


# this is only for practice

import matplotlib.pyplot as plt
import numpy as np

img=plt.imread('E:\\COLLEGE 5TH SEM\\college\\prac7_class\\high.jpeg')

if len(img.shape)==3:
    img=np.mean(img,axis=2).astype(np.uint8)

global_threshold=int(np.mean(img))
global_thresholded=(img>=global_threshold)*255

plt.figure(figsize=(10,5))
plt.subplot(121)
plt.title('original image')
plt.imshow(img,cmap='gray')

plt.subplot(122)
plt.title('global thresholding')
plt.imshow(global_thresholded,cmap='gray')

plt.show()