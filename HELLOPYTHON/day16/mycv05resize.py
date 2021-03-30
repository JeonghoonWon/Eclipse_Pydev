import cv2
import numpy as np

img = cv2.imread('0.jfif', 1)
img_28 = cv2.resize(img,(28,28))
img_gray = cv2.cvtColor(img_28, cv2.COLOR_BGR2GRAY)
img_input = (255 - img_gray)/256
img_input2 =  np.reshape(img_input,(1,28*28))

print(img_input2)
print(img_input2.shape)

cv2.imshow('Test Image', img_input)
cv2.waitKey(0)
cv2.destroyAllWindows()

