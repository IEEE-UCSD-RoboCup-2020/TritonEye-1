import cv2
import numpy as np

ball = cv2.imread('theBall.png')
h, w, c = ball.shape
gray_img = cv2.cvtColor(ball, cv2.COLOR_BGR2GRAY)
img = cv2.medianBlur(gray_img, 3)
cimg = cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)

circles = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,1, w / 8,

                           param1=100,param2=30,minRadius=10,maxRadius=100)

circles = np.uint16(np.around(circles))

for i in circles[0,:]:
   # draw the outer circle
   cv2.circle(ball,(i[0],i[1]),i[2],(0,255,0),2)
   print(ball[i[0], i[1]])
   # draw the center of the circle
   cv2.circle(ball,(i[0],i[1]),2,(0,0,255),3)

cv2.imwrite("test.png", ball)
#cv2.imshow("HoughCirlces", ball)
cv2.waitKey()
cv2.destroyAllWindows()