import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# Load the image
image_path = 'E:\\COLLEGE 5TH SEM\\college\\6_class\\lamborghini.jpg'
image = mpimg.imread(image_path)

# Convert image to grayscale if it's in color
if len(image.shape) == 3:
    image = np.mean(image, axis=2).astype(np.uint8)

# Global Thresholding
global_threshold = np.median(image)
global_thresholded = (image >= global_threshold) * 255

# Local Thresholding with Median Filter
block_size = 11
height, width = image.shape
local_thresholded = np.zeros_like(image, dtype=np.uint8)

for i in range(0, height, block_size):
    for j in range(0, width, block_size):
        block = image[i:i + block_size, j:j + block_size]
        threshold = np.median(block)
        local_thresholded[i:i + block_size, j:j + block_size] = (block >= threshold) * 255

# Display the original grayscale image, the globally thresholded image, and the locally thresholded image
plt.figure(figsize=(15, 5))

plt.subplot(131)
plt.title('Gray Image')
plt.imshow(image, cmap='gray')

plt.subplot(132)
plt.title('Global Thresholding')
plt.imshow(global_thresholded, cmap='gray')

plt.subplot(133)
plt.title('Local Thresholding (Median)')
plt.imshow(local_thresholded, cmap='gray')

plt.tight_layout()
plt.show()
