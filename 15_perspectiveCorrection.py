import cv2
import numpy as np

from util_pick import get_four_points

image = cv2.imread('data/images/book1.jpg')
# cv2.imshow('original', image)

point_src = get_four_points(image) # 점은 시계방향으로 지정하는 것을 기본으로함.

print(point_src)

# 변환할 비어있는 이미지를 생성
dst_size = (300, 400, 3)

image_dst = np.zeros(dst_size, np.uint8)

point_dst = np.array([0,0, 300,0, 300,400, 0,400])
point_dst = point_dst.reshape(4, 2)

matrix, status = cv2.findHomography(point_src, point_dst)
result = cv2.warpPerspective(image, matrix, (300, 400))
cv2.imshow('result', result)

cv2.waitKey(0)
cv2.destroyAllWindows()