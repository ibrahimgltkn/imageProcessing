import cv2
import numpy as np
from google.colab.patches import cv2_imshow

def Gamma(src, gamma):
    iGamma = 1 / gamma
    table = [((i / 255) ** iGamma) * 255 for i in range(256)]
    table = np.array(table, np.uint8)

    return cv2.LUT(src, table)


img = cv2.imread('example.jpeg')
gamma_image1 = Gamma(img, 3.0)
gamma_image2 = Gamma(img, 4.0)
gamma_image3 = Gamma(img, 5.0)

cv2.putText(gamma_image1, "gamma={3.0}", (10, 30),
		cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 3)

cv2.putText(gamma_image2, "gamma={4.0}", (10, 30),
		cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 3)

cv2.putText(gamma_image3, "gamma={5.0}", (10, 30),
		cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 3)
        

cv2_imshow(np.hstack((img,gamma_image1,gamma_image2,gamma_image3)))