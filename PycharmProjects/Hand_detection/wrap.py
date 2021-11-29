import cv2
import numpy as np

img = cv2.imread("card.jpg")

width,height= 350,250
pts1 = np.float32([[422,118],[156,214],[214,380],[482,283]])
pts2= np.float32([[width,0],[0,0],[0,height],[width,height]])
matrix = cv2.getPerspectiveTransform(pts1,pts2)
imgoutput = cv2.warpPerspective(img,matrix,(width,height))

cv2.imshow("Image",img)
cv2.imshow("output",imgoutput)
cv2.waitKey(0)