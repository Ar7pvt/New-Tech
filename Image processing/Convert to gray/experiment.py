from PIL import Image
import matplotlib.pyplot as plt
from convert import grayscale
import numpy as np

image=plt.imread("E:\\college\\2_class\\low.jpg")
gray_image=grayscale(image)

plt.imshow(gray_image,cmap="gray")
plt.show()

im_array=np.array(gray_image)

padding_width=100
padded_array=np.pad(im_array,padding_width,mode="constant")

padded_image=Image.fromarray(padded_array)
plt.imshow(padded_image,cmap="gray")
plt.show()
