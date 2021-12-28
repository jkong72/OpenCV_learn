import cv2
import numpy as np

# 이미지의 컬러 정보를 가져온다.
source = cv2.imread('data/imges/sample.jpg', 1) # 인자를 1로 해도 컬러 정보를 가져온다.

print (cv2.IMREAD_COLOR) # 실제로 인자 자체가 1의 값을 갖는것을 알 수 있다.

# 이미지 크기 조정 (resize)

# 가로는 80%,
# 세로는 60%만큼 확대/축소

scaleX = 0.8
scaleY = 0.6

scaleDown = cv2.resize(source, None, fx=scaleX, fy=scaleY, interpolation=cv2.INTER_LINEAR)
#interpolation은 사이즈가 변하면서(주로 커지면서) 생기는 공백을 채우는 방법론을 지정하는 파라미터

print (scaleDown)

cv2.imshow('Original', source)
cv2.imshow('scaled Down', scaleDown)


# 이미지 자르기 (Crop)
# 이미지는 행렬 데이터이므로, 자르기는 슬라이싱을 통해서 간단하게 얻을 수 있다.
crop_image = source[10:200, 150:250]

cv2.imshow('Crop img', crop_image)

cv2.waitKey(0)
cv2.destroyAllWindows()