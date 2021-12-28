import cv2
import numpy as np

source = cv2.imread('data/images/sample.jpg')


# 이미지 정보 범위를 0~255에서 0~1로 정규화함.
scailingFactor = 1/255.0 
source = source * scailingFactor

print (source)

# 정규화한 데이터를 복호화
source = source * 255
print (source)
# 하지만 위 배열에 포함된 자료형은 "실수"자료형이다.
# 따라서 해당 배열은 이미지로 읽어들일 수 없다.

source = source.astype(int)
print (source)