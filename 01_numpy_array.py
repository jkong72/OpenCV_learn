import cv2
import numpy as np

print ('-'*15)
print ('Code Start here\n')

print ('-'*15)
print ('1차원 배열')
# 1차원 배열 만들기
arr = np.array([5, 10, 15])

print (arr)         # 배열 출력
print (arr.shape)   # 형태 출력
print (arr[0])      # 내부 자료에 접근

arr[1] = 50         # 내부 자료 변경
print (arr)

print ('-'*15)
print ('2차원 배열')
# 2차원 배열 만들기
arr_2d = np.array([[5, 6, 1, 2, 9, 10]])
arr_2d = arr_2d.reshape(3,2)

print (arr_2d)
print (arr_2d[0])      # 내부 자료에 접근
print (arr_2d[0][1])
print (arr_2d[ 1, 1])

print ('-'*15)
print ('컬러 read')
# 이미지 파일을 컬러(BGR)로 읽어오기
img = cv2.imread('data/images/sample.jpg')
print (img)
print (img.shape)
print (img.ndim)

print ('-'*15)
print ('그레이스케일 read')
# 이미지 파일을 그레이스케일로 읽어오는 방법
img2 = cv2/cv2.imread('data/images/sample.jpg', flags=0)
print (img2)
print (img2.shape)
print (img2.ndim)