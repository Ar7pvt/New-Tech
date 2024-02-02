import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

image=mpimg.imread('E:\\COLLEGE 5TH SEM\\Image processing\\6_class\\lamborghini.jpg')

if len(image.shape)==3:
    image=np.mean(image,axis=2).astype(np.uint8)

hist,bins=np.histogram(image,bins=256,range=(0,256))
hist_prob=hist/float(image.size)
cumsum_prob=np.cumsum(hist_prob)
mean_intensity=np.sum(np.arange(256)*hist_prob)
best_threshold=0
max_variance=0

for threshold in range(1,256):
    prob1=cumsum_prob[threshold]
    prob2=1-prob1
    mean1=np.sum(np.arange(threshold)*hist_prob[:threshold])/prob1
    mean2=(mean_intensity-(prob1*mean1))/prob2
    between_class_variance=prob1*prob2*(mean1-mean2)**2
    if between_class_variance > max_variance:
        max_variance=between_class_variance
        best_threshold=threshold

otsu_thresholded=(image>=best_threshold)*255

plt.figure(figsize=(10,5))

plt.subplot(121)
plt.title('original image')
plt.imshow(image,cmap='gray')

plt.subplot(122)
plt.title("otsu's image")
plt.imshow(otsu_thresholded,cmap='gray')

plt.tight_layout()
plt.show()

