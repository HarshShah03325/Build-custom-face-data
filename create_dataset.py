from imutils.video import VideoStream
import argparse
import imutils
import os
import cv2
import time

ap = argparse.ArgumentParser()
ap.add_argument("-c", "--cascade", required=True,
	help = "path to where the face cascade resides")
ap.add_argument("-o", "--output", required=True,
	help="path to output directory")
args = vars(ap.parse_args())

detector = cv2.CascadeClassifier(args["cascade"])
print("[INFO] Starting video stream...")
# vs = VideoStream(0).start()
vs = cv2.VideoCapture(-1)
time.sleep(2)
total=0

if not vs.isOpened():
    print("Cannot open camera:")
    exit()


while True:
    
    ret,frame = vs.read()
    
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    # frame = vs.read()
    orig = frame.copy()
    frame = imutils.resize(frame, width=400)

    rects = detector.detectMultiScale(
		cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY), scaleFactor=1.1, 
		minNeighbors=5, minSize=(30, 30))

    for (x, y, w, h) in rects:
	    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    cv2.imshow('frame',frame)
    
    key = cv2.waitKey(1) & 0xFF
    if key == ord("k"):
        print(str(total+1)+" image captured!")
        p = os.path.sep.join([args["output"], "{}.png".format(
	    str(total).zfill(5))])
        cv2.imwrite(p,orig)
        total+=1

    elif key == ord("q"):
    	break

print("[INFO] {} face images stored".format(total))
print("[INFO] cleaning up...")
cv2.destroyAllWindows()




     
