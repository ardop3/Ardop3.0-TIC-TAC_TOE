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
from std_msgs.msg import Int16

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

a = [0,0,0,0,0,0,0,0,0]

k =0

board  =  [' ' for x in range(10)]

def insert_letter (letter,pos):

  board[pos] = letter


def index(x,y, prev_location):
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

	return prev_location










def detector():

		gray = cv2.cvtColor(cv_image, cv2.COLOR_BGR2GRAY) 
		location = 50	  
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
		        #cv2.imshow("Detected Circle", cv_image) 

		        location = index(a,b, location)
		        #self.pub.publish(location)

		        #print(location)

		    return location


def free_space(pos):

  return board[pos] == ' '

def print_board(board):
    print('===========================')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('===========================')

def is_winner_detected(board,letter):

  return (board[7]== letter and board[8]== letter and board[9]==letter) or (board[4]== letter and board[5]== letter and board[6]==letter) or (board[1]== letter and board[2]== letter and board[3]==letter) or (board[1]== letter and board[4]== letter and board[7]==letter) or (board[2]== letter and board[5]== letter and board[8]==letter) or (board[3]== letter and board[6]== letter and board[9]==letter) or (board[1]== letter and board[5]== letter and board[9]==letter) or (board[3]== letter and board[5]== letter and board[7]==letter)


def player_move():




		iter1 = True

		  
		while iter1:

			location_player = detector()


			if free_space(int(location_player)):

			    iter1 = False
			    insert_letter('O', int(location_player))











def main1():
  
  print_board(board)
  print("entered main")
  #insert_letter('O', int(n))


  while not is_board_full(board):




    if not is_winner_detected(board,'O'):  ##  computer x, human o

      #insert_letter('O', int(n))
      player_move()
      print_board(board)
    
    else:
      print('Human wins')
      break

    if not is_winner_detected(board,'X'):  ##  computer o, human x
      move = ARDOP_move()
      insert_letter('X', move)
      print_board(board)
    
    else:
      print('ARDOP wins')
      break





    
  if is_board_full(board):
    print('TIE')



def ARDOP_move():
    possibleMoves = [x for x, letter in enumerate(board) if letter == ' ' and x != 0] # Create a list of possible moves
    move = 0
    
    
    for let in ['O','X']:
        for i in possibleMoves:
            boardCopy = board[:]
            boardCopy[i] = let
            if is_winner_detected(boardCopy, let):
                move = i
                return move


    
    corner_avalaible = []
    for i in possibleMoves:
        if i in [1,3,7,9]:
            corner_avalaible.append(i)
    if len(corner_avalaible) > 0:
        move = selectRandom(corner_avalaible)
        return move
    
    
    if 5 in possibleMoves:
        move = 5
        return move

    
    edges_avalaible = []
    for i in possibleMoves:
        if i in [2,4,6,8]:
            edges_avalaible.append(i)
    
    if len(edges_avalaible) > 0:
        move = selectRandom(edges_avalaible)

    return move

import random

def selectRandom(L):
  ln =len(L)
  r = random.randrange(0,ln)
  return L[r]



def is_board_full(board):

  if board.count(' ') > 1:
    return False
  else:
    return True





class image_converter:

  def __init__(self):

    self.image_pub = rospy.Publisher("image_topic_2",Image) 
    self.pub = rospy.Publisher('Board_Index', Int16, queue_size=10)

    
    self.bridge = CvBridge()
    self.image_sub = rospy.Subscriber("/camera/rgb/image_color",Image,self.callback)


  def callback(self,data):
    try:

    	global cv_image
    	cv_image = self.bridge.imgmsg_to_cv2(data, "bgr8")
    	rate = rospy.Rate(30)
    	#location_callback = detector()
    	#ain1(location_callback)
    	main1()
    	'''
		gray = cv2.cvtColor(cv_image, cv2.COLOR_BGR2GRAY)
		circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1.8, 100)
		
		if circles is not None:
			# convert the (x, y) coordinates and radius of the circles to integers
			circles = np.round(circles[0, :]).astype("int")
			 
				# loop over the (x, y) coordinates and radius of the circles
			for (x, y, r) in circles:
			# draw the circle in the output image, then draw a rectangle
			# corresponding to the center of the circle
				cv2.circle(cv_image, (x, y), r, (0, 255, 0), 4)
				cv2.rectangle(cv_image, (x - 5, y - 5), (x + 5, y + 5), (0, 128, 255), -1)
		



		
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
		        #cv2.imshow("Detected Circle", cv_image) 

		        location = index(a,b)
		        #self.pub.publish(location)

		        print(location)

		        main1(int(location))
		        #rate.sleep()
		        
		'''


    except CvBridgeError as e:
      print(e)

    (rows,cols,channels) = cv_image.shape
    if cols > 60 and rows > 60 :
      cv2.circle(cv_image, (50,50), 10, 255)

    #cv2.imshow("Image window", cv_image)
    cv2.waitKey(3)

    try:
      self.image_pub.publish(self.bridge.cv2_to_imgmsg(cv_image, "bgr8"))
    except CvBridgeError as e:
      print(e)

def main(args):
  ic = image_converter()

  rospy.init_node('image_converter', anonymous=True)
  
  #rospy.init_node('index_sender', anonymous = True)


  try:
    rospy.spin()
  except KeyboardInterrupt:
    print("Shutting down")
  cv2.destroyAllWindows()

if __name__ == '__main__':

	main(sys.argv)
