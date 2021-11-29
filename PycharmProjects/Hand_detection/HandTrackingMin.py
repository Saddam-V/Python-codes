import cv2
import mediapipe as mp
import time

video = cv2.VideoCapture(0,cv2.CAP_DSHOW)
#video.set(3,640) #length
#video.set(4,480) #breadth
#video.set(10,100) #brightness

mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

pTime = 0
cTime =0

while True:
    success, img = video.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    print(results.multi_hand_landmarks)

    if results.multi_hand_landmarks:
        for handlms in results.multi_hand_landmarks:
            for id, lm in enumerate(handlms.landmark):
                #print(id,lm)
                h,w,c = img.shape
                cx,cy = int(lm.x*w), int(lm.y*h)
                print(id,cx,cy)
                if id == 12:
                    cv2.circle(img,(cx,cy),15,(300,0,300),cv2.FILLED)
            mpDraw.draw_landmarks(img, handlms, mpHands.HAND_CONNECTIONS)

    cTime = time.time()
    fps = 1/(cTime - pTime)
    pTime = cTime

    cv2.putText(img,str(int(fps)),(10,70), cv2.FONT_HERSHEY_SIMPLEX,3,
                (255,0,155),3)

    cv2.imshow("Image", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break