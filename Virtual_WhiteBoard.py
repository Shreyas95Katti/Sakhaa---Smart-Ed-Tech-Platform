import cv2
import numpy as np
import time
import os
import HandTrackingModule as htm

folderPath = "Header"
myList = os.listdir(folderPath)
print(myList)
overlayList = []

for imPath in myList:
    image = cv2.imread(f'{folderPath}/{imPath}')
    overlayList.append(image)

header = overlayList[8]


cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)

detector = htm.handDetector(detectionCon = 0.85)

while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)

    #Find HandLandmarks
    frame = detector.fingHands(frame)
    lmList = detector.findPosition(frame, draw = False)

    if len(lmList) != 0:
        x1, y1 = lmList[8][1:]         #Tip of index
        x2, y2 = lmList[12][1:]        #Tip of Middle

        
        #Check for Fingers
        fingers = detector.fingersUp()
        #print(fingers)

        #If select 2 finger
        if fingers[1] and fingers[2]:
            print("Selection Mode")

        #If draw 1 finger
        if fingers[1] and fingers[2] == False:
            print("Drawing Mode")
    
    #Setting Header
    frame[0:125, 0:1280] = header
    cv2.imshow("Frame", frame)
    if cv2.waitKey(1) == 27:
        break