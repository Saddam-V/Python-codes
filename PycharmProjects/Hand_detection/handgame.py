import cv2
import mediapipe as mp
import time
import HandDetectionModule as hm
import os
import pyttsx3
engine = pyttsx3.init()
file = open('text.txt','r+')
engine.setProperty('rate', 110)

pTime = 0
cTime = 0
video = cv2.VideoCapture(0, cv2.CAP_DSHOW)
detector = hm.handDetector()

while True:
    success, img = video.read()
    img = detector.findHands(img)
    lmList = detector.findPosition(img, draw = False)
    cx,cy = detector.coordinates(8,img)
    if len(lmList) !=0:
        print(lmList[4])

    if cx in range(1,130) and cy in range(1,130):
        break

    if cx in range(500,600) and cy in range(260,460):
        engine.say(each)
        print(each)
        engine.runAndWait()



    if cx in range(100,300) and cy in range(200,460):
        each = file.readline()
        engine.say(each)
        print(each)
        engine.runAndWait()




    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime


    cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 3,
                (255, 0, 155), 3)

    cv2.imshow("Image", img)
    time.sleep(0.8)
    cv2.waitKey(20)
