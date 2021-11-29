import  cv2
import numpy as np #for dialation and erotion

img= cv2.imread("pic.jpg")
kernel = np.ones((5,5),np.uint8) #for dialation and erotion

imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) #to gray the image
imgBlur = cv2.GaussianBlur(imgGray,(7,7),0)  #to blur image
imgCanny = cv2.Canny(img,100,100) #to find borders
imgDialation = cv2.dilate(imgCanny,kernel,iterations=1) #for dialation
imgEroded = cv2.erode(imgDialation,kernel,iterations=1) #for erotion


cv2.imshow("Gray_Image",imgGray)
cv2.imshow("Blur_Image",imgBlur)
cv2.imshow("Canny_Image",imgCanny)
cv2.imshow("Dialaton_Image",imgDialation)
cv2.imshow("Eroded_Image",imgEroded)
cv2.waitKey(0)

