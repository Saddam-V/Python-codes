import os
from fer import FER
import matplotlib.pyplot as plt
import cv2


# define a video capture object
def emotion():
    try:
        cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
        success, frame = cap.read()
        cv2.imwrite("frame.jpg",frame)
        # Display the resulting frame
        # cv2.imshow('frame', frame)
        # cv2.waitKey(3)
        img = plt.imread("frame.jpg")
        detector = FER(mtcnn=True)
        emotion, score = detector.top_emotion(img)
        print(emotion,score)
        # plt.imshow(img)
        os.remove("frame.jpg")
        cap.release()
        cv2.destroyAllWindows()
        return emotion
    except:
        print("Error Occured")