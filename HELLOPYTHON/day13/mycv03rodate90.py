import cv2


# 이미지 읽기
img = cv2.imread('image/lena.png',1)
img90 = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE) # 시계방향으로 90도 회전
print(img90) 
# 이미지 화면에 표시
cv2.imshow('Test Image', img90)
cv2.waitKey(0)

# 이미지 윈도우 삭제
cv2.destroyAllWindows()
 
