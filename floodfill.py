import cv2
import numpy as np
#input
src = cv2.imread("input\\200_0.png")
hsv = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)
Binary1 = cv2.inRange(hsv, (20,0,63),(101,255,255))#去除觀眾

kernel = np.ones((3,3), np.uint8)
result = cv2.morphologyEx(Binary1,cv2.MORPH_OPEN, kernel)
masked_gray = cv2.bitwise_and(src,src, mask = result)

def onmouse(event,x,y,flags,parm):
    if event==cv2.EVENT_LBUTTONDOWN:
        copyIma = masked_gray.copy()
        h, w = src.shape[:2]
        mask = np.zeros([h+2, w+2], np.uint8)
        #cv2.floodFill(output,input,選定pixel位置,新顏色,往下範圍,往上範圍,flags)
        cv2.floodFill(copyIma, mask, (x,y), (0, 0,255), (53, 26, 63), (65, 88, 80), cv2.FLOODFILL_FIXED_RANGE)
        
        cv2.imshow("1", copyIma)
        cv2.waitKey(0)
cv2.imshow("input",masked_gray)
cv2.setMouseCallback("input",onmouse)
cv2.waitKey(0)