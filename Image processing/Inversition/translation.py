import matplotlib.pyplot as plt
import numpy as np
import cv2
img = plt.imread('2_class\\imag.jpg')
img2 = np. zeros_like(img)

img2[300:, 500:] = img[:-300, :-500]
plt.imshow(img2)
plt.show()

def translation_img(src_img,shift_distance,shape_of_out_image):
    h,w=src_img.shape[:2]
    x_distance=shift_distance[0]
    y_distance=shift_distance[1]
    ts_mat=np.array([[1,0,x_distance],[0,1,y_distance]])

    out_img=np.zeros(shape_of_out_image,dtype='u1')

    for i in range(h):
        for j in range(w):
            origin_x=j
            origin_y=i
            origin_xy=np.array([origin_x,origin_y,1])

            new_xy=np.dot(ts_mat,origin_xy)
            new_x=new_xy[0]
            new_y=new_xy[1]

            if 0<new_x<w and 0<new_y<h:
                out_img[new_y,new_x]=src_img[i,j]
    return out_img

shift_distance=(500,300)
shifted_image=translation_img(img,shift_distance,img.shape)

plt.imshow(img)
plt.show()
plt.imshow(shifted_image)
plt.show()

