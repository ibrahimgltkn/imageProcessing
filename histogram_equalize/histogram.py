import cv2
import numpy as np
from matplotlib import pyplot as plt
from google.colab.patches import cv2_imshow

image=cv2.imread('example.jpeg',0)

h_image=cv2.equalizeHist(image) 

cv2_imshow(np.hstack((image,h_image))) 
plt.show()
plt.hist(h_image.ravel(),256,[0,256]);  
plt.show()