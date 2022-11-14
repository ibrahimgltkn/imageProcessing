import cv2
import numpy as np
from google.colab.patches import cv2_imshow
 
image = cv2.imread('bluer.png',1) 
image1 = cv2.blur(image,(5,5))
image2 = cv2.boxFilter(image,-1,(2,2),normalize=True) 

cv2_imshow(np.hstack((image1,image2)))