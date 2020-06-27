#!/usr/bin/env python
from __future__ import print_function

import roslib
#roslib.load_manifest('my_package')
import sys
import rospy
import cv2
from std_msgs.msg import String
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError

from collections import deque

import numpy as np
import argparse

import imutils
import time


location = 0 
p_00 = [193, 166]
p_01 =[233,164]
p_02=[273,162]
p_03 =  [312, 160]
p_04=[194, 193]
p_05=[234, 190]
p_06=[273, 188]
p_07=[313, 187]
p_08=[195, 220]
p_09=[234,219]
p_10=[276, 217]
p_11=[314, 214]
p_12=[196, 248]
p_13=[236, 245]
p_14=[277, 243]
p_15= [313,242]


a=0
b=0
c=0
d=0
e=0
f=0
g=0
h=0
i=0

def index(x,y):
	#print("in")


	if ((p_00[0] <= x <= p_01[0]) and (p_00[1] <= y <= p_04[1]) and (a == 0)):

		k =1 
		a = +1
		return k

	if ((p_01[0] <= x <= p_02[0]) and (p_01[1] <= y <= p_05[1]) and (b == 0)):

		k =2 
		b = +1
		return k
	if ((p_02[0] <= x <= p_03[0]) and (p_02[1] <= y <= p_06[1]) and (c == 0)):

		k =3 
		c = +1
		return k

	if ((p_04[0] <= x <= p_05[0]) and (p_04[1] <= y <= p_08[1]) and (d == 0)):

		k =4 
		d = +1
		return k

	if ((p_05[0] <= x <= p_06[0]) and (p_05[1] <= y <= p_09[1]) and (e == 0)):

		k =5 
		e = +1
		return k

	if ((p_06[0] <= x <= p_07[0]) and (p_06[1] <= y <= p_10[1]) and (f == 0)):

		k =6 
		f = +1
		return k

	if ((p_08[0] <= x <= p_09[0]) and (p_08[1] <= y <= p_12[1]) and (g == 0)):

		k =7
		g = +1
		return k

	if ((p_09[0] <= x <= p_10[0]) and (p_09[1] <= y <= p_13[1]) and (h == 0)):

		k =8 
		h = +1
		return k

	if ((p_10[0] <= x <= p_11[0]) and (p_10[1] <= y <= p_14[1]) and (i == 0)):

		k =9 
		i = +1
		return k




class image_converter:



  def __init__(self):


  	self.bridge = CvBridge()
  	self.image_sub = rospy.Subscriber("/camera/rgb/image_color",Image,self.callback)

  def callback(self,data):
    try:


		cv_image = self.bridge.imgmsg_to_cv2(data, "bgr8")

		gray = cv2.cvtColor(cv_image, cv2.COLOR_BGR2GRAY) 
		  
		# Blur using 3 * 3 kernel. 
		gray_blurred = cv2.blur(gray, (3, 3)) 
		  
		# Apply Hough transform on the blurred image. 
		detected_circles = cv2.HoughCircles(gray_blurred,  
		                   cv2.HOUGH_GRADIENT, 1, 20, param1 = 40, 
		               param2 = 30, minRadius = 1, maxRadius = 25) 
		  
		# Draw circles that are detected. 
		if detected_circles is not None: 
		  
		    # Convert the circle parameters a, b and r to integers. 
		    detected_circles = np.uint16(np.around(detected_circles)) 
		  
		    for pt in detected_circles[0, :]: 
		        a, b, r = pt[0], pt[1], pt[2] 
		  
		        # Draw the circumference of the circle. 
		        cv2.circle(cv_image, (a, b), r, (0, 255, 0), 2) 
		  
		        # Draw a small circle (of radius 1) to show the center. 
		        cv2.circle(cv_image, (a, b), 1, (0, 0, 255), 3) 
		        
		        cv2.imshow("Detected Circle", cv_image) 
		        #print("send")

		        location = index(a,b)
		        print(location)





    except CvBridgeError as e:
      print(e)



def main(args):
  ic = image_converter()
  rospy.init_node('image_converter', anonymous=True)
  try:
    rospy.spin()
  except KeyboardInterrupt:
    print("Shutting down")
  cv2.destroyAllWindows()

if __name__ == '__main__':


		main(sys.argv)