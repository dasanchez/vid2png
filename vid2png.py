import cv2
import sys

"""
	Open a video file and display all the frames in it.
	Usage: vid2png filename scale skip
	Only every [skip] frames will be read.
	Each image will be divided by [scale] before saving to disk.
	
"""
cv2.namedWindow('Video Display')
cap = cv2.VideoCapture(sys.argv[1])
# Calculate new size
w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)/int(sys.argv[2]))
h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)/int(sys.argv[2]))
frame_total = cap.get(cv2.CAP_PROP_FRAME_COUNT)
print(frame_total, w, h)
pic_name = sys.argv[1]
pic_name = pic_name[:-4]
print(pic_name)
frame_count = 0

while cap.isOpened():
    ret,frame = cap.read()
    if ret:
        if frame_count%int(sys.argv[3]) == 0:
            filename = pic_name + str(frame_count).zfill(4) + '.png'
            frame = cv2.resize(frame, (w,h), interpolation = cv2.INTER_AREA)
            cv2.imwrite(filename,frame)
            #print(filename)
        frame_count += 1
            #cv2.imshow('Video Display', frame)
    else:
        break

cap.release()
cv2.destroyAllWindows()

