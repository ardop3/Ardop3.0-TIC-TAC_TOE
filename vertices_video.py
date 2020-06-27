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



class image_converter:

  def __init__(self):
    self.image_pub = rospy.Publisher("image_topic_2",Image)

    self.bridge = CvBridge()
    self.image_sub = rospy.Subscriber("/camera/rgb/image_color",Image,self.callback)

  def callback(self,data):
    
    try:

      cv_image = self.bridge.imgmsg_to_cv2(data, "bgr8")
      #img = cv2.imread(cv_image)
      img = cv2.cvtColor(cv_image,cv2.COLOR_BGR2GRAY)
      _, threshold = cv2.threshold(img, 200, 235, cv2.THRESH_BINARY) 
      _, contours, _= cv2.findContours(threshold, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
      font = cv2.FONT_HERSHEY_COMPLEX 
      i = 1
      for cnt in contours : 
		  
		    #approx = cv2.approxPolyDP(cnt, 0.009 * cv2.arcLength(cnt, True), True) 
        peri = cv2.arcLength(cnt, True)
        approx = cv2.approxPolyDP(cnt, 0.003 * peri, True)
        #cv2.drawContours(cv_image, [approx], -1, (0, 0, 255), 2) 
        area = cv2.contourArea(cnt)
        #print( area, len(approx))
        if len(approx) > 30  and area > 1100  :	

            i = 0
            n = approx.ravel()
            #print(n)     

           
            for j in n : 
                if(i % 40 == 0): 
                    x = n[i] 
                    y = n[i + 1] 
          
                    # String containing the co-ordinates. 
                    string = str(x) + " " + str(y)  
                    #print(string)
                    if(i == 0): 
                        # text on topmost co-ordinate. 
                        print((x,y))
                        #cv2.putText(cv_image, "Arrow tip", (x, y), 
                        #                font, 0.1, (255, 0, 0))  
                        image = cv2.circle(cv_image,(x,y) , 2, (0,0,255) , 3)
                    else: 
                        # text on remaining co-ordinates. 
                        #cv2.putText(cv_image, string, (x, y),  
                        #          font, 0.1, (0, 0, 255))  
                        #print((x,y))
                        image = cv2.circle(cv_image,(x,y) , 2, (0,0,255) , 1)
                i = i + 1 

                   
	    
          
          #i = i +1
      print("-------------")  
      cv2.imshow('cv_image',1)


    except CvBridgeError as e:
      print(e)

    (rows,cols,channels) = cv_image.shape
    if cols > 60 and rows > 60 :
      cv2.circle(cv_image, (50,50), 10, 255)

    cv2.imshow("Image window", cv_image)
    cv2.waitKey(3)

    try:
      self.image_pub.publish(self.bridge.cv2_to_imgmsg(cv_image, "bgr8"))
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

