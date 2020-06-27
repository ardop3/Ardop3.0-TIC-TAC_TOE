import random
#!/usr/bin/env python
import rospy
from std_msgs.msg import UInt16
from time import sleep
import sys
from geometry_msgs.msg import Twist
from array import *

'''
def define_solution(index):

    IK = Twist()

    extra_y = 0
    extra_z = 0

    Ik = [[ 0, 16+extra_y ,45 +extra_z ] , 
           [ 16, 21+extra_y ,38 +extra_z] , 
           [ 27, 32+extra_y ,28 +extra_z] , 
           [ 0, 0+extra_y ,57 +extra_z ] , 
           [ 19, 5+extra_y ,51 +extra_z] , 
           [ 32, 18+extra_y ,36 +extra_z] ,   
           [ 0, -19+extra_y ,72+extra_z ] ,  
            [25, -12+extra_y ,69+extra_z ] ,
              [ 39, 0+extra_y ,57+extra_z ]  ]




    IK.linear.x = Ik[index+1][0]
    IK.linear.y = Ik[index+1][1]
    Ik.linear.z = Ik[index+1][2]
    Ik.angular.x = 0
    Ik.angular.y = 0
    Ik.angular.z = 0

    Ik_solution.publish(  IK)


'''


def Ik_pass():

    rospy.init_node('Ik_publisher', anonymous=True)
    Ik_solution = rospy.Publisher('/Ik_result', Twist, queue_size=10)

    k = int (input( " enter index"))
    index = k

    IK = Twist()

    e1 = 14
    e2 = 14
    e3 = 12


    e4 = 9
    e5 = 9+5
    e6 = 10+5


    e7 = 5
    e8 = 9
    e9 = 9

    extra_z = 1


    


    Ik_sol = [[ -3, 57+e1 ,4 +extra_z ] , 
           [ 9, 55+e2 ,19 +extra_z] , 
           [ 22, 63+e3 ,14 +extra_z] , 


           [ 0, 28+e4 ,35 +extra_z ] , 
           [ 10, 33+e5 ,27 +extra_z] , 
           [ 23, 45+e6 ,21 +extra_z] ,  


           [ 0, 3+e7 ,64+extra_z ] ,  
            [16, 9+e8 ,57+extra_z ] ,
              [ 25, 25+e9 ,38+extra_z ] ,


           [-45 , 60 , 90]    ]




    a = Ik_sol[index-1][0]
    b=  Ik_sol[index-1][1]
    c = Ik_sol[index-1][2]

    print ( a,b, c)



    IK.linear.x = a
    IK.linear.y = b
    IK.linear.z = c
    IK.angular.x = 0
    IK.angular.y = 0
    IK.angular.z = 0

    Ik_solution.publish(  IK)


if __name__ == '__main__':
    try:
        #Testing our function
        Ik_pass()
    except rospy.ROSInterruptException: pass



