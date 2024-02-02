# Q2. Given an image, perform the following operations to it:
#     a. Global thresholding and local thresholding for a block size of 10 with a constant value
#        of 3 for thresholding correction.
#     b. Otsu’s method for thresholding grayscale image into binary image.
#     c. Once you have performed the binary image conversion, write a Python script to find
#        out area (Pixel distribution) within the entire binary image and output it as a
#        percentage.

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import cv2

image=mpimg.imread('E:\\COLLEGE 5TH SEM\\college\\6_class\\lamborghini.jpg')

#converting image to gray
if len(image.shape)==3:
    image=np.mean(image,axis=2).astype(np.uint8)

global_threshold=int(np.mean(image))
global_thresholded=(image>=global_threshold)*255

block_size=10 
constant_c=3

height,width=image.shape
local_thresholded=np.zeros_like(image,dtype=np.uint8)
for i in range(0,height,block_size):
    for j in range(0,width,block_size):
        block=image[i:i + block_size, j:j +block_size]
        block_mean=np.mean(block)
        threshold=block_mean-constant_c
        local_thresholded[i:i+block_size,j:j+block_size]=(block>=threshold)*255

# ret, otsu_thresholded = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

hist, bins = np.histogram(image, bins=256, range=(0, 256))
pmf = hist / np.sum(hist)
max_variance = 0
best_threshold = 0
total_mean = np.sum(np.arange(256) * pmf)

for threshold in range(256):
    prob1 = np.sum(pmf[:threshold])
    prob2 = np.sum(pmf[threshold:])
    
    mean1 = np.sum(np.arange(threshold) * pmf[:threshold]) / prob1 if prob1 > 0 else 0
    mean2 = np.sum(np.arange(threshold, 256) * pmf[threshold:]) / prob2 if prob2 > 0 else 0
    
    between_class_variance = prob1 * prob2 * (mean1 - mean2) ** 2
    if between_class_variance > max_variance:
        max_variance = between_class_variance
        best_threshold = threshold

otsu_thresholded=(image>=best_threshold)*255


total_pixels = image.size
white_pixels = np.count_nonzero(image == 1)
percentage_area = (white_pixels / total_pixels) * 100
print(f"Percentage of white pixels (area) in the binary image: {percentage_area:.2f}%")

plt.figure(figsize=(10,5))
plt.subplot(141)
plt.title('gray image')
plt.imshow(image,cmap='gray')

plt.subplot(142)
plt.title('global thresholding')
plt.imshow(global_thresholded,cmap='gray')

plt.subplot(143)
plt.title('local thresholding')
plt.imshow(local_thresholded,cmap='gray')

plt.subplot(144)
plt.title('Otsu Thresholding')
plt.imshow(otsu_thresholded, cmap='gray')

plt.tight_layout()
plt.show()
