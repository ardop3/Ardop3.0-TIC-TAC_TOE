#!/usr/bin/env python
from __future__ import print_function

import roslib

import sys
import rospy
import cv2
from std_msgs.msg import String
from std_msgs.msg import UInt16
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
import numpy as np
'''


p_00 = [258, 126]
p_01 =[296,125]
p_02=[337,126]
p_03 =  [274,125]
p_04=[258,154]
p_05=[296,153]
p_06=[336,153]
p_07=[374,150]
p_08=[256,182]
p_09=[296,182]
p_10=[335,182]
p_11=[373,180]
p_12=[256,207]
p_13=[295,207]
p_14=[333,207]
p_15= [374,207]

a = [0,0,0,0,0,0,0,0,0]

k =0

def index(x,y):
  #print("in")
  global k

  if ((p_00[0] <= x <= p_01[0]) and (p_00[1] <= y <= p_04[1]) and (a[0] == 0)):

    k =1 
    a[0] = +1 
    #pub.publish(k)
    #main1(k)
    return k

  if ((p_01[0] <= x <= p_02[0]) and (p_01[1] <= y <= p_05[1]) and (a[1] == 0)):

    k =2 
    a[1] = +1
    #pub.publish(k)
    #main1(k)

    return k


  if ((p_02[0] <= x <= p_03[0]) and (p_02[1] <= y <= p_06[1]) and (a[2] == 0)):

    k =3 
    a[2] = +1
    #pub.publish(k)
    #main1(k)
    return k

  if ((p_04[0] <= x <= p_05[0]) and (p_04[1] <= y <= p_08[1]) and (a[3] == 0)):

    k =4 
    a[3] = +1
    #pub.publish(k)
    #main1(k)
    return k

  if ((p_05[0] <= x <= p_06[0]) and (p_05[1] <= y <= p_09[1]) and (a[4] == 0)):

    k =5 
    a[4] = +1
    #pub.publish(k)
    #main1(k)
    return k

  if ((p_06[0] <= x <= p_07[0]) and (p_06[1] <= y <= p_10[1]) and (a[5] == 0)):

    k =6 
    a[5] = +1
    #pub.publish(k)
    #main1(k)
    return k

  if ((p_08[0] <= x <= p_09[0]) and (p_08[1] <= y <= p_12[1]) and (a[6] == 0)):

    k =7
    a[6] = +1
    #pub.publish(k)
    #main1(k)
    return k

  if ((p_09[0] <= x <= p_10[0]) and (p_09[1] <= y <= p_13[1]) and (a[7] == 0)):

    k =8 
    a[7] = +1
    #pub.publish(k)
    #main1(k)
    return k

  if ((p_10[0] <= x <= p_11[0]) and (p_10[1] <= y <= p_14[1]) and (a[8] == 0)):

    k =9 
    a[8]= +1
    #pub.publish(k)
    #main1(k)
    return k

  return k

'''




class image_converter:

  def __init__(self):


    self.p_00 = [156, 290]
    self.p_01 =[206,288]
    self.p_02=[259,284]
    self.p_03 =  [311,281]


    self.p_04=[153,325]
    self.p_05=[206,322]
    self.p_06=[259,319]
    self.p_07=[312,315 ]

    self.p_08=[150,363]
    self.p_09=[204,360]
    self.p_10=[259,356]
    self.p_11=[314,354]

    self.p_12=[147,401]
    self.p_13=[202,399]
    self.p_14=[260,396]
    self.p_15= [316,393]

    self.k = 15
    self.a = [0,0,0,0,0,0,0,0,0]
 
    self.image_pub = rospy.Publisher("image_topic_2",Image)
    self.pub = rospy.Publisher('index', UInt16, queue_size=1)

    self.bridge = CvBridge()
    self.image_sub = rospy.Subscriber("/camera/rgb/image_color",Image,self.callback)

  def index(self,x,y):


      if ((self.p_00[0] <= x <= self.p_01[0]) and (self.p_00[1] <= y <= self.p_04[1]) and (self.a[0] == 0)):

        self.k =1 
        self.a[0] = +1 
        #self.pub.publish(self.k)
        #main1(k)
        print(self.k)
        return self.k

      if ((self.p_01[0] <= x <= self.p_02[0]) and (self.p_01[1] <= y <= self.p_05[1]) and (self.a[1] == 0)):

        self.k =2 
        self.a[1] = +1
        #self.pub.publish(self.k)
        #main1(k)
        print(self.k)

        return self.k


      if ((self.p_02[0] <= x <= self.p_03[0]) and (self.p_02[1] <= y <= self.p_06[1]) and (self.a[2] == 0)):

        self.k =3 
        self.a[2] = +1
        #self.pub.publish(self.k)
        #main1(k)
        print(self.k)
        return self.k

      if ((self.p_04[0] <= x <= self.p_05[0]) and (self.p_04[1] <= y <= self.p_08[1]) and (self.a[3] == 0)):

        self.k =4 
        self.a[3] = +1
        #self.pub.publish(self.k)
        #main1(k)
        print(self.k)
        return self.k

      if ((self.p_05[0] <= x <= self.p_06[0]) and (self.p_05[1] <= y <= self.p_09[1]) and (self.a[4] == 0)):

        self.k =5 
        self.a[4] = +1
        #self.pub.publish(self.k)
        #main1(k)
        print(self.k)
        return self.k

      if ((self.p_06[0] <= x <= self.p_07[0]) and (self.p_06[1] <= y <= self.p_10[1]) and (self.a[5] == 0)):

        self.k =6 
        self.a[5] = +1
        #self.pub.publish(self.k)
        #main1(k)
        print(self.k)
        return self.k

      if ((self.p_08[0] <= x <= self.p_09[0]) and (self.p_08[1] <= y <= self.p_12[1]) and (self.a[6] == 0)):

        self.k =7
        self.a[6] = +1
        #self.pub.publish(self.k)
        #main1(k)
        print(self.k)
        return self.k

      if ((self.p_09[0] <= x <= self.p_10[0]) and (self.p_09[1] <= y <= self.p_13[1]) and (self.a[7] == 0)):

        self.k =8 
        self.a[7] = +1
        #self.pub.publish(self.k)
        #main1(k)
        print(self.k)
        return self.k

      if ((self.p_10[0] <= x <= self.p_11[0]) and (self.p_10[1] <= y <= self.p_14[1]) and (self.a[8] == 0)):

        self.k =9 
        self.a[8]= +1
        #self.pub.publish(self.k)
        #main1(k)
        print(self.k)
        return self.k

      self.pub.publish(self.k) 
      return self.k   



  def callback(self,data):
    try:
      cv_image = self.bridge.imgmsg_to_cv2(data, "bgr8")

      gray = cv2.cvtColor(cv_image, cv2.COLOR_BGR2GRAY) 
      # Blur using 3 * 3 kernel. 
      gray_blurred = cv2.blur(gray, (3, 3)) 
        
      # Apply Hough transform on the blurred image. 
      detected_circles = cv2.HoughCircles(gray_blurred,  
                   cv2.HOUGH_GRADIENT, 1, 40, param1 = 100, 
               param2 = 30, minRadius = 1, maxRadius = 20) 
        
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

              location = self.index(a,b)
              #print(location)

    except CvBridgeError as e:
      print(e)


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