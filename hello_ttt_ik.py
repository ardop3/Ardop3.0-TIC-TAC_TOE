import random
#!/usr/bin/env python
import rospy
from std_msgs.msg import UInt16
from time import sleep
import sys
from geometry_msgs.msg import Twist
from array import *

board  =  [' ' for x in range(10)]

i = 1

def insert_letter (letter,pos):

  board[pos] = letter


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

  return ((board[7]== letter and board[8]== letter and board[9]==letter) or
  (board[4]== letter and board[5]== letter and board[6]==letter) or 
  (board[1]== letter and board[2]== letter and board[3]==letter) or 
  (board[1]== letter and board[4]== letter and board[7]==letter) or
  (board[2]== letter and board[5]== letter and board[8]==letter) or
  (board[3]== letter and board[6]== letter and board[9]==letter) or
  (board[1]== letter and board[5]== letter and board[9]==letter) or 
  (board[3]== letter and board[5]== letter and board[7]==letter) )


def is_board_full(board):

    if board.count(' ') > 1:
        return False

    else:

        return True

def Human_Move(data):

    run = True
    move = data.data

    move = int(move)
    #print(move)
    if not(is_winner_detected(board , 'X')):
        if free_space(move):
            print(move)
            run = False
            insert_letter( 'O', move)
            temp_move = move
            print_board(board)
            ARDOP_play()
        else:
            pass
    else:
        print("ARDOP WON")
        sys.exit()
    



def ARDOP_move():

    possible_moves = [ x for x , letter in enumerate(board)  if letter == ' '  and x!= 0]

    move  = 0

    for  let  in [ 'X' , 'O']: # x and o inverted from orignial code
        for i in possible_moves:
            board_copy = board[:]
            board_copy[i] = let
            if is_winner_detected(board_copy , let):
                move = i
                a1,b1,c1 = send_IK(move)
                return move


    cornersOpen = []

    for i in possible_moves:
        if i in [1,3,7,9]:
            cornersOpen.append(i)

    if len(cornersOpen) > 0:

        move = selectRandom(cornersOpen)
        a1,b1,c1 = send_IK(move)

        return move

    if 5 in possible_moves:
        move = 5
        a1,b1,c1 = send_IK(move)
        return move



    edgesOpen = []

    for i in possible_moves:
        if i in [2,4,6,8]:
            edgesOpen.append(i)

    if len(edgesOpen) > 0:

        move = selectRandom(edgesOpen)
        a1,b1,c1 = send_IK(move)

        return move

    return move

def send_IK(index):

    Ik_solution = rospy.Publisher('/Ik_result', Twist, queue_size=10)

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
              [ 25, 25+e9 ,38+extra_z ]  ]


    a = Ik_sol[index-1][0]
    b=  Ik_sol[index-1][1]
    c = Ik_sol[index-1][2]

    



    IK.linear.x = a
    IK.linear.y = b
    IK.linear.z = c
    IK.angular.x = 0
    IK.angular.y = 0
    IK.angular.z = 0

    Ik_solution.publish( IK)
    print ( a,b, c  , index)

    return a,b,c


def selectRandom(L):
    ln = len(L)
    r = random.randrange(0 , ln)
    return L[r]

def dummy_pass():

    dummy_Ik_solution = rospy.Publisher('/Ik_result', Twist, queue_size=10)

    IK2 = Twist()

    m=0

    IK2.linear.x = 0
    IK2.linear.y =0
    IK2.linear.z = 0
    IK2.angular.x = 0
    IK2.angular.y = 0
    IK2.angular.z = 0

    dummy_Ik_solution.publish( IK2)

    return m


def ARDOP_play():

        if not(is_winner_detected(board , 'O')): ## make ardop  move given human has not won
            move = ARDOP_move()
            #a1,b1,c1 = send_IK(move)
            

            if move == 0:

                print('TIE')
            else:
                #a1,b1,c1 = send_IK(move)
                insert_letter('X', move)
                print_board(board)
        else :
            print(" Human won")



def working():

        if not(is_winner_detected(board , 'X')): ## make player move given ardop has not won

            rospy.Subscriber("index", UInt16, Human_Move)
            


            #print_board(board)
        else :
            print(" ARDOP won")

        rospy.spin()
            






def main():

        print_board(board)
        rospy.init_node('Tick_Tack_Toe', anonymous=True)
        a2 = dummy_pass()
        global temp_move 
        temp_move = 15
        working()




if __name__ == '__main__':


    main()


'''


    while not (is_board_full(board)):

        if not(is_winner_detected(board , 'X')): ## make player move given ardop has not won
            Human_Move()
            print_board(board)
        else :
            print(" ARDOP won")
            break


        if not(is_winner_detected(board , 'O')): ## make ardop  move given human has not won
            move = ARDOP_move()

            if move == 0:

                print('TIE')
            else:
                insert_letter('X', move)
                print_board(board)
        else :
            print(" Human won")
            break

    if  (is_board_full(board)):
        print("TIE")
'''