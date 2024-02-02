import numpy as np
import matplotlib.pyplot as plt

def grayscale(image):
    height,width=image.shape[:2]
    grayimage=np.zeros((height,width),dtype=np.uint8)

    for i in range(height):
        for j in range(width):
            red=image[i,j,0]
            green=image[i,j,1]
            blue=image[i,j,2]
            gray_value=0.3*red+0.59*green+0.11*blue
            grayimage[i,j]=gray_value
    return grayimage

# if __name__=="__main__":
image=plt.imread("E:\\COLLEGE 5TH SEM\\Image processing\\3_class\\low.jpg")
plt.figure(figsize=(12,6))
plt.subplot(121)
plt.title("Original image")
plt.imshow(image)

image=grayscale(image)
plt.subplot(122)
plt.title("Gray image")
plt.imshow(image,cmap='gray')
plt.show()
