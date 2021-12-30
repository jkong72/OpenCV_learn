import cv2
import numpy as np

image = cv2.imread('data/images/mark.jpg')

cv2.imshow('img', image)



# 파일 위에 선 그리기
imageLine = image.copy() # 원본 파일과 분리된 배열을 생성 (복사)
cv2.line(imageLine, (322,179), (400,183), (125, 22, 255), 10, cv2.LINE_AA)
cv2.imshow('img Line', imageLine)

# 파일 위에 원 그리기
imageCircle = image.copy()
cv2.circle(imageCircle, (350,200), 150, (123, 212, 18), 4, cv2.LINE_AA)
cv2.imshow('img Circle', imageCircle)

# 파일 위에 타원 그리기
imageEllipse = image.copy()
cv2.ellipse(imageEllipse, (360,200), (100,170), 45, 0, 460, (56, 177, 132), 2)
cv2.ellipse(imageEllipse, (360,200), (100,170), 135, 0, 360, (12, 212, 189), 3)
cv2.imshow('img Ellipses', imageEllipse)

# 파일 위에 사각형 그리기
imageRectangle = image.copy()
cv2.rectangle(imageRectangle, (208,55), (450,355), (255, 12, 23), 3)
cv2.imshow ('img Rectangle', imageRectangle)

# 파일 위에 글자 삽입
imageText = image.copy()
cv2.putText(imageText, 'Mark Zuckerberg.', (205,50), cv2.FONT_HERSHEY_SIMPLEX, 1, (77,177,13), 2)
cv2.imshow('text', imageText)

cv2.waitKey(0)
cv2.destroyAllWindows()