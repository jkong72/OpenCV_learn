import cv2

image = cv2.imread('data/images/sample.jpg')
print(image.shape)
cv2.imshow('original', image)

# 회전시킬 이미지를 만들기 위한 정보
center = (image.shape[1] /2, image.shape[0] /2) # 각 축의 절반에 해당하는 지점 = 중앙
rotationAngle = 30 # 회전 각도
scaleFactor = 1 # 확대 배율

# 회전 정보를 담고 있는 행렬을 가져온다.
matrix = cv2.getRotationMatrix2D(center, rotationAngle, scaleFactor)

print (matrix)

# 이미지를 회전 정보 행렬에 대입해 회전한다.
result = cv2.warpAffine(image, matrix, (image.shape[1], image.shape[0]))
cv2.imshow('rotation', result)

cv2.waitKey(0)
cv2.destroyAllWindows()