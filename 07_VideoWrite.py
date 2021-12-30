import cv2
import numpy as np

# 캠 및 연결된 영상기록장치로부터 데이터를 가져오기
cap = cv2.VideoCapture(0, )

if cap.isOpened() == False:
    print('카메라로부터 정보를 얻을 수 없습니다.')
else:
    # 프레임의 정보를 가져오기
    # 화면크기를 말하는 것 (width, height)
    frame_width = int( cap.get(3))
    frame_height = int( cap.get(4))

    print (frame_width, frame_height)

    out = cv2.VideoWriter('data/videos/output.avi', # 파일 경로와 이름
                            cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'), # 압축정보.
                            10, # FPS
                            (frame_width, frame_height)) # 프레임 크기 정보
    # 캠으로부터 사진(영상)을 계속 입력받으며 화면에 표시 및
    # 위의 out에 저장.

    while True :
        ret, frame = cap.read()
        if ret == True :
            cv2.imshow('Video', frame) # 화면에 표시
            out.write(frame)

            if cv2.waitKey(10) & 0xFF == 27: # esc를 누르면 탈출.
                break
        else:
            break
    cap.release()
    out.release()
    cv2.destroyAllWindows
