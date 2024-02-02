import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

image=Image.open('E:\\COLLEGE 5TH SEM\\college\\6_class\\lamborghini.jpg')
image=image.convert('L')

image_array=np.array(image)

initialthreshold=127

previous_threshold=0
current_threshold=initialthreshold

epsilon=12.0
while abs(current_threshold-previous_threshold)>epsilon:
    segmented_image=(image_array>current_threshold)*255
    mean1=np.mean(image_array[segmented_image==0])
    mean2=np.mean(image_array[segmented_image==255])
    prev_threshold=current_threshold
    current_threshold=(mean1+mean2)/2

plt.figure(figsize=(12,6))
plt.subplot(121)
plt.title('original image')
plt.imshow(image_array,cmap='gray')

plt.subplot(122)
plt.title('segmented image')
plt.imshow(segmented_image,cmap='gray')

plt.show()