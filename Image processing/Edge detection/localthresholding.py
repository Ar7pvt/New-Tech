import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

image=mpimg.imread("E:\\COLLEGE 5TH SEM\\Image processing\\6_class\\lamborghini.jpg")

# converting image to gray scale
if len(image.shape)==3:
    image=np.mean(image,axis=2).astype(np.uint8)

#global thresholding
global_threshold=127
global_thresholded=(image>=global_threshold)*255


#local thresholding
block_size=11  
constant_c=2

height,width=image.shape
local_thresholded=np.zeros_like(image,dtype=np.uint8)
for i in range(0,height,block_size):
    for j in range(0,width,block_size):
        block=image[i:i + block_size, j:j +block_size]
        block_mean=np.mean(block)
        threshold=block_mean-constant_c
        local_thresholded[i:i+block_size,j:j+block_size]=(block>=threshold)*255

plt.figure(figsize=(10,5))
plt.subplot(131)
plt.title('original image')
plt.imshow(image,cmap='gray')

plt.subplot(132)
plt.title('global thresholding')
plt.imshow(global_thresholded,cmap='gray')

plt.subplot(133)
plt.title('local thresholding')
plt.imshow(local_thresholded,cmap='gray')

plt.tight_layout()
plt.show()