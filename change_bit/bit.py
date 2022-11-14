import cv2
import numpy as np
from matplotlib import pyplot as plt
from google.colab.patches import cv2_imshow

image = cv2.imread('example.jpeg',cv2.IMREAD_GRAYSCALE)

image8=image/(255/8)
image16=image/(255/16)
image24=image/(255/24)

cv2.putText(image8, "bit={8}", (10, 30),
		cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 0, 0), 3)
cv2.putText(image16, "bit={16}", (10, 30),
		cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 0, 0), 3)
cv2.putText(image24, "bit={24}", (10, 30),
		cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 0, 0), 3)

cv2_imshow(np.hstack((image,image8,image16,image24)))

plt_org=plt.hist(image.ravel(),256,[0,256]);

plt_8=plt.hist(image8.ravel(),256,[0,256]);

plt_16=plt.hist(image16.ravel(),256,[0,256]);

plt_24=plt.hist(image24.ravel(),256,[0,256]);