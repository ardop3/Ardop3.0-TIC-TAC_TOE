#!/usr/bin/env python
from __future__ import print_function
from matplotlib import pyplot as plt
import cv2
import numpy as np
import roslib
import sys
import rospy
from std_msgs.msg import String
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError


img = cv2.imread('grid.PNG', 0)

print(type(img))



img2 = cv2.imread('grid.PNG')



_, threshold = cv2.threshold(img, 110, 255, cv2.THRESH_BINARY) 


_, contours, _= cv2.findContours(threshold, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)




font = cv2.FONT_HERSHEY_COMPLEX 

for cnt in contours : 
  
    approx = cv2.approxPolyDP(cnt, 0.009 * cv2.arcLength(cnt, True), True) 
  

    cv2.drawContours(img2, [approx], 0, (0, 0, 255), 5)  
  
 
    n = approx.ravel()  
    i = 0
    print(n)


plt.imshow(img2)
plt.show()


