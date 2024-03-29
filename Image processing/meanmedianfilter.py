import numpy as np
import matplotlib.pyplot as plt
import random
import cv2

def SaltAndPepper(image, density):
    output = np.zeros(image.shape, np.uint8)
    threshold = 1- density
    
    # range (0,0) to (h-1,w-1)
    for i in range(image.shape[0]):
          for j in range(image.shape[1]):
               possibility = random.random()
               if possibility < density:
                    output[i][j] = 0
               elif possibility > threshold:
                    output[i][j] = 255
               else:
                    output[i][j] = image[i][j]
    return output

def MeanFilter(image, filter_size):
     height, width = image.shape
     output = np.zeros((height, width),np.uint8)
     result = 0

     #filter size
     if  filter_size == 9:   # (1,1) starting pt
          for j in range(1,image.shape[0]-1):
                for i in range(1,image.shape[1]-1):
                    for y in range(-1 ,2):
                         for x in range(-1,2):
                              result += image[j+y, i+x]
                    output[j][i] =   int(result / filter_size)  # making blanck space
                    result = 0

     elif filter_size == 25: #(2,2) starting pt
             for j in range(2,image.shape[0]-2):
                for i in range(2,image.shape[1]-2):
                    for y in range(-2 ,3):
                         for x in range(-2,3):
                              result += image[j+y, i+x]
                    output[j][i] =   int(result / filter_size)
                    result = 0

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



image = cv2.cvtColor(cv2.imread('c:\\Users\\TUF\\\Desktop\\Lenna_(test_image).png'), cv2.COLOR_BGR2GRAY)
# img = plt.imread(image/Fruits.jpg)

plt.imshow(image, cmap = 'gray')
plt.show()
imageWithNoise=SaltAndPepper(image, 0.1)
plt.imshow(imageWithNoise, cmap='gray')
plt.show()
mean_3x3_lenna = MeanFilter(imageWithNoise, 25)
new_image = mean_3x3_lenna
plt.imshow(mean_3x3_lenna, cmap='gray')
plt.show()  
medium = MedianFilter(imageWithNoise, 9)
plt.imshow(medium, cmap='gray')
plt.show()

        

       
             
        


                          




