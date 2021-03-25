import cv2


# 이미지 읽기
img = cv2.imread('image/red.png',1)
#img = cv2.imread('image/red.png',2)

img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

print(img_gray) 
# 이미지 화면에 표시
cv2.imshow('Test Image', img)
cv2.waitKey(0)

# 이미지 윈도우 삭제
cv2.destroyAllWindows()
 
