# import numpy as np
# import matplotlib.pyplot as plt

# from convert import grayscale
# def calculate_histogram(image):
#     height,width=image.shape[:2]

#     histogram=np.zeros(256,dtype=int)

#     for i in range (height):
#         for j in range(width):
#             grayscale_level=image[i,j]
#             histogram[grayscale_level]+=1
    
#     return histogram


# def plot_histogram(histogram):
#     plt.imshow(histogram)
#     plt.show()

# def cumulativesum(histogram):
#     return np.cumsum(histogram)

# def histogram_equation(image):
#     histogram=calculate_histogram(image)

#     cdf=cumulativesum(histogram)
#     height,width=image.shape[:2]
#     new_image=np.zeros_like(image)

#     for i in range(height):
#         for j in range(width):
#             greyscale_level=image[i,j]
#             new_pixel_value=cdf[greyscale_level]*255
#             new_image[i,j]=new_pixel_value
#     return new_image

# if __name__=="__main__":
#     image=plt.imread("E:\\COLLEGE 5TH SEM\\Image processing\\7prac_class\\high.jpeg")

#     gray_image=grayscale(image)

#     histogram=calculate_histogram(gray_image)
#     plt.imshow(image,cmap='gray')
#     plt.show()
#     plot_histogram(histogram)

#     equalized_image=histogram_equation(gray_image)

#     equalized_histogram=calculate_histogram(equalized_image)

#     plt.imshow(equalized_image,cmap='gray')
#     plt.show()
#     plot_histogram(equalized_histogram)

import numpy as np
import matplotlib.pyplot as plt

def calculate_histogram(image):
    height, width = image.shape[:2]
    histogram = np.zeros(256, dtype=int)

    for i in range(height):
        for j in range(width):
            grayscale_level = image[i, j]
            histogram[grayscale_level] += 1

    return histogram

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

def plot_histogram(histogram,gray):
    plt.figure(figsize=(12,6))
    plt.subplot(121)
    plt.title("gray image ")
    plt.imshow(gray,cmap='gray')

    plt.subplot(122)
    plt.plot(histogram, color='black')
    plt.title('Histogram')
    plt.xlabel('Pixel Value')
    plt.ylabel('Frequency')
    plt.show()

if __name__ == "__main__":
    # Load your image here (replace "your_image_path" with the actual path)
    image_path = "E:\\COLLEGE 5TH SEM\\Image processing\\7prac_class\\high.jpeg"
    image = plt.imread(image_path)
    
    gray=grayscale(image) #converting image to grayscale

    # If the image has three channels (RGB), convert it to grayscale
    if len(image.shape) == 3:
        image = np.dot(image[..., :3], [0.2989, 0.5870, 0.1140])
    

    # Convert to integer type (assuming pixel values are in the range [0, 1])
    image = (image * 255).astype(np.uint8)

    # Calculate and plot the histogram
    histogram = calculate_histogram(image)
    plot_histogram(histogram,gray)
