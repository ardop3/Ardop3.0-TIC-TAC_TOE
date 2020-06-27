#!/usr/bin/env python
# license removed for brevity
import rospy
from std_msgs.msg import Int16


board  =  [' ' for x in range(10)]

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

  return (board[7]== letter and board[8]== letter and board[9]==letter) or (board[4]== letter and board[5]== letter and board[6]==letter) or (board[1]== letter and board[2]== letter and board[3]==letter) or (board[1]== letter and board[4]== letter and board[7]==letter) or (board[2]== letter and board[5]== letter and board[8]==letter) or (board[3]== letter and board[6]== letter and board[9]==letter) or (board[1]== letter and board[5]== letter and board[9]==letter) or (board[3]== letter and board[5]== letter and board[7]==letter)

def main(n):
  
  print_board(board)

  while not is_board_full(board):
    '''
    if not is_winner_detected(board,'X'):  ##  computer o, human x
      move = ARDOP_move()
      insert_letter('O', move)
      print_board(board)
    
    else:
      print('Human wins')
      break
    
    '''

    if not is_winner_detected(board,'O'):  ##  computer o, human x
      player_move(n)
      print_board(board)
    
    else:
      print('ARDOP wins')
      break

    if not is_winner_detected(board,'X'):  ##  computer o, human x
      move = ARDOP_move()
      insert_letter('X', move)
      print_board(board)
    
    else:
      print('Human wins')
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

def player_move(n):

    move = n
    if free_space(int(move)):

      insert_letter('O', int(move))


#main()



def callback(data):
    main(data.data)
    
def listener():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('Board', anonymous=True)


    rospy.Subscriber("Board_Index", Int16, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()


