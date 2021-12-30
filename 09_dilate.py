import cv2

image = cv2.imread('data/images/truth.png')

cv2.imshow('original', image)

# dilation 이란 이미지의 확장을 의미한

dilationSize = 6

# 확장 구조를 정의
element = cv2.getStructuringElement(cv2.MORPH_RECT, (2*dilationSize, 2*dilationSize))

imageDilate = cv2.dilate(image, element)

cv2.imshow('dilation', imageDilate)

cv2.waitKey(0)
cv2.destroyAllWindows()

##########
image = cv2.imread('data/images/sample.jpg')
cv2.imshow('original', image)
element = cv2.getStructuringElement(cv2.MORPH_CROSS, (2*dilationSize, 2*dilationSize))
imageDilate = cv2.dilate(image, element)
cv2.imshow('dilation', imageDilate)

cv2.waitKey(0)
cv2.destroyAllWindows()