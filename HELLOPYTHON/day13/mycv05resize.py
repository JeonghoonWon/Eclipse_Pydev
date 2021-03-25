import cv2

src = cv2.imread('image/lena.png', cv2.IMREAD_COLOR)

img_50 = cv2.resize(src, dsize=(50, 50), interpolation=cv2.INTER_AREA) #절대크기
dst2 = cv2.resize(src, dsize=(0, 0), fx=0.5, fy=0.5, interpolation=cv2.INTER_LINEAR) #상대크기

print(img_50)
print(img_50.shape)
#cv2.imshow("src", src)
cv2.imshow("img_50", img_50)
#cv2.imshow("dst2", dst2)
cv2.waitKey()
cv2.destroyAllWindows()