import cv2


# 이미지 읽기
img = cv2.imread('image/lena.png',2)
print(img) 
# 이미지 화면에 표시
cv2.imshow('Test Image', img)
cv2.waitKey(0)

cv2.imwrite('image/lena2.jpg', img)


# 이미지 윈도우 삭제
cv2.destroyAllWindows()
 
