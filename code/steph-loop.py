import cv2

# Open video 
cap = cv2.VideoCapture('/Users/marcosalvalaggio/Desktop/steph-loop/steph.mp4')

# Fps, size of video  
fps = cap.get(cv2.CAP_PROP_FPS)
size = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),
        int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))

# Count of frames 
frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
duration = frame_count/fps

# Video features 
print('fps = ' + str(fps))
print('number of frames = ' + str(frame_count))
print('duration (S) = ' + str(duration))
minutes = int(duration/60)
seconds = duration%60
print('duration (M:S) = ' + str(minutes) + ':' + str(seconds))

# Clips loop 
i = 0
frame_set_no = 0

for i in range(0,100):
    videoWriter = cv2.VideoWriter(
      'good'+str(i)+'.avi', cv2.VideoWriter_fourcc('M','J','P','G'), fps, size)
    
    cap.set(cv2.CAP_PROP_POS_FRAMES, frame_set_no)

    success, frame = cap.read()
    numFramesRemaining = 3 * fps - 1  # 3 seconds for clip 
    while numFramesRemaining > 0:
        if frame is not None:
            videoWriter.write(frame)
        success, frame = cap.read()
        numFramesRemaining -= 1
    
    frame_set_no = frame_set_no + (3 * fps - 1)
