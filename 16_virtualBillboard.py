import cv2
import numpy as np

from util_pick import get_four_points

image = cv2.imread('data/images/first-image.jpg')
image_dst = cv2.imread('data/images/times-square.jpg')

# cv2.imshow('Original', image) # 이미지 확인
# cv2.imshow('dst', image_dst)  # 이미지 확인

image_x = image.shape[1]    # 삽입할 이미지의 가로(x축)길이
image_y = image.shape[0]    # 삽입할 이미지의 세로(y축)길이
print (image_x, image_y)    # 값이 맞는지 확인
point_src = np.array([0,0, image_x,0, image_x,image_y, 0,image_y], dtype=float)
point_src = point_src.reshape(4, 2)

point_dst = get_four_points(image_dst) #

matrix, status = cv2.findHomography(point_src, point_dst)
image_temp = cv2.warpPerspective(image, matrix, (image_dst.shape[1], image_dst.shape[0]))
# cv2.imshow('result', result) # 제대로 바뀌었는지 이미지를 확인 

# 이미지의 합성
cv2.fillConvexPoly(image_dst, point_dst.astype(int), (0,0,0)) # 합성 영역을 0(검은색)으로 바꾼다.
# cv2.imshow('img to 0', image_dst) # 제대로 바뀌었는지 이미지를 확인

result = image_temp + image_dst # 두 이미지를 합성. 서로 겹치는 영역이 0(검은색)으로 설정되었으므로 합성할 수 있음.
cv2.imshow('result', result)

cv2.waitKey(0)
cv2.destroyAllWindows()