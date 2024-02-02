from numpy import cumsum as cumulativesum
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
            grayimage[i,j]=0.3*red+0.58*green+0.11*blue
    return grayimage

def calculate_histogram(image):
    height,width=image.shape[:2]

    histogram=np.zeros(256,dtype=int)

    for i in range (height):
        for j in range(width):
            grayscale_level=image[i,j]
            histogram[grayscale_level]+=1
    
    return histogram


def plot_histogram(histogram):
    plt.imshow(histogram)
    plt.show()

def histogram_equation(image):
    histogram=calculate_histogram(image)

    cdf=cumulativesum(histogram)
    height,width=image.shape[:2]
    new_image=np.zeros_like(image)

    for i in range(height):
        for j in range(width):
            greyscale_level=image[i,j]
            new_pixel_value=cdf[greyscale_level]*255
            new_image[i,j]=new_pixel_value
    return new_image

if __name__=="__main__":
    image=plt.imread("E:\\COLLEGE 5TH SEM\\college\\7prac_class\\high.jpeg")

    gray_image=grayscale(image)

    histogram=calculate_histogram(gray_image)
    print(histogram.shape)
    plt.imshow(gray_image,cmap='gray')
    plt.show()
    # plt.imshow(histogram)
    # plt.show()

    equalized_image=histogram_equation(gray_image)

    equalized_histogram=calculate_histogram(equalized_image)

    plt.imshow(equalized_image,cmap='gray')
    plt.show()
    plot_histogram(equalized_histogram)