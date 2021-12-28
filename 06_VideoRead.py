import cv2
import numpy as np

# FPS : Frame per Second, 1초당 노출되는 프레임(사진)

# 비디오 파일 읽기
cap = cv2.VideoCapture('data/videos/chaplin.mp4')

if cap.isOpened() == False:
    print ('파일을 여는데 실패했습니다.')
else:
    # 동영상은 시간에 따른 사진의 집합이므로
    # 동영상 시작부터 끝까지 imshow를 반복하면 동영상을 재생할 수 있다.
    while cap.isOpened() :
        ret, frame = cap.read() # 사진을 1장씩 가져옴
                                # ret = 데이터가 제대로 있는지 여부
                                # frame = 사진
        if ret == True :    # 읽을 수 없는 프레임이거나 더이상 프레임이 없을 때 까지.
            cv2.imshow("Video", frame)
            if cv2.waitKey(1000) & 0xFF ==27 : # 파라미터는 키를 입력받기까지의 대기시간으로 동영상에서 0을 입력하면 1프레임에서 영원히 키 입력을 대기한다. 그 외의 수를 넣으면, 해당 밀리초 만큼씩 대기하므로, 재생 FPS를 조정하는 효과를 볼 수도 있다.
                break                        # 27번키 (esc)를 입력받으면 창을 닫는다.
        else :
            break
    cap.release()
    cv2.destroyAllWindows()