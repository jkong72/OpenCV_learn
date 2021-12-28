import cv2
import numpy as np

img_file = 'data/images/sample.jpg'

# OpenCV를 통해 이미지 열기 (BGR 컬러 정보)
image = cv2.imread(img_file, cv2.IMREAD_COLOR)

# 이미지가 정상인지 체크하는 코드
if image is None :
    print ('이미지 파일을 열 수 없습니다.')
else:
    print(image.shape)

# OpenCV 에서는 이미지 정보를 BGR순서로 읽어온다.
# 따라서 불러온 이미지를 그레이 스케일로 변경할 수 있다.

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) 

cv2.imshow('color', image) # 이미지를 표시하는 함수
# 하지만 CPU는 읽어들인 코드는 바로 잊어버리기 때문에
# 실행된 순간 바로 종료되어 버린다.

# 따라서 제대로 확인할 수 있도록
# CPU의 코드 실행을 잠시 멈춘다.
cv2.waitKey(0)              # 키 입력을 받을 때까지 CPU를 붙잡는 함수
cv2.destroyAllWindows()     # cv2가 실행한 모든 창을 닫는 함수

# 새로운 창 띄우기
cv2.imshow ('color', image)
cv2.imshow ('gray scale', gray_image)

cv2.waitKey(0)
cv2.destroyAllWindows()