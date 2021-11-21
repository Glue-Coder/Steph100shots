import cv2


cap = cv2.VideoCapture('/Users/marcosalvalaggio/Desktop/steph-loop/steph.mp4')

fps = cap.get(cv2.CAP_PROP_FPS)
size = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),
        int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))

frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

duration = frame_count/fps

###################

i = 0
frame_set_no = 25

for i in range(0,100):

    cap.set(cv2.CAP_PROP_POS_FRAMES, frame_set_no)

    status, frame = cap.read()

    if status == False:
            break
    cv2.imwrite('good_frame'+str(i)+'.png',frame)

    frame_set_no = frame_set_no + 90
