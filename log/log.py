import cv2
import numpy as np
from google.colab.patches import cv2_imshow

image = cv2.imread('example.jpeg')
c = 255 / np.log(1 + np.max(image)) 
image_log = c * (np.log(image + 1))

cv2_imshow(np.hstack((image,image_log)))