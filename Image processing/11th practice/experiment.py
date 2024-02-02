import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# Load the image
image_path = 'E:\\COLLEGE 5TH SEM\\college\\6_class\\lamborghini.jpg'
image = mpimg.imread(image_path)


if len(image.shape) == 3:
    image = np.mean(image, axis=2).astype(np.uint8)

def calculate_entropy(image):
    histogram, _ =no.histogram(image.flatten(),bins=265,range=(0,256))
    probabilities=histogram / float(image.size)
    non_zero_probabilities=probabilities[probabilities>0]
    entropy= -np.sum(non_zero_probabilities * np.log2(non_zero_probabilities))
    return entropy

def calculate_local_homogenetiy(image):
    mean_gray_value=np.mean(image)
    std_deviation=np.std(image)
    homogenity=1/(1+std_deviation)
    return homogenity

def calculate_contrast(image):
    histogram, _ =np.histogram(image.flatten(),bins=265,range=(0,256))
    min_pixel_value=np.min(image)
    max_pixel_value=np.max(image)
    contrast=max_pixel_value-min_pixel_value
    return contrast

histogram, _ =np.histogram(image.flatten(),bins=256,range=(0,256))
normalized_histogram=histogram/float(image.size)
entropy=-np.sum(normalized_histogram[normalized_histogram>0]*np.log2(normalized_histogram))

homogenity=calculate_local_homogenetiy(image)

contrast = calculate_contrast(image)

plt.figure(figsize=(15, 5))

plt.subplot(131)
plt.title('Gray Image')
plt.imshow(image, cmap='gray')


plt.subplot(132)
plt.bar(range(256),normalized_histogram,color='gray')
plt.title('normalize histogram ')


plt.subplot(133)
plt.text(0.1,0.8, f'Entropy: {entropy:.2f}\n Homogenity: {homogenity:.2f}\nContrast: {contrast}',fontsize=12 )
plt.title('Entropy, Homogenity,and contrast')


plt.show()
