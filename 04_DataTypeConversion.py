import cv2
import numpy as np

source = cv2.imread('data/images/sample.jpg')
cv2.imread('경로/파일.확장자')

# 이미지 정보 범위를 0~255에서 0~1로 정규화함.
scailingFactor = 1/255.0 
source = source * scailingFactor

print (source)

# 정규화한 데이터를 복호화
source = source * 255
print (source)
# 하지만 위 배열에 포함된 자료형은 "실수"자료형이다.
# 0~1사이의 값으로 나누는 동안 1이하의 "실수"자료형으로 변환된 것이다.
# 따라서 해당 배열은 이미지로 읽어들일 수 없다.

# 수치 자체는 올바르게 출력되었으므로
# 아래 두가지 방법중 하나를 사용해 자료형을 형변환 한다.
source = np.uint8(source)
print (source)

source = source.astype(int)
print (source)