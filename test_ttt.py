import random


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

def Human_Move():

    run = True

    while run:
        move = input(' enter value')
        try:
            move = int(move)
            if free_space(move):
                run = False
                insert_letter( 'O', move)
            else:
                print("space occupied")

        except:

            print("invalid input")


def ARDOP_move():

    possible_moves = [ x for x , letter in enumerate(board)  if letter == ' '  and x!= 0]

    move  = 0

    for  let  in [ 'O' , 'X']:
        for i in possible_moves:
            board_copy = board[:]
            board_copy[i] = let
            if is_winner_detected(board_copy , let):
                move = i
                return move


    cornersOpen = []

    for i in possible_moves:
        if i in [1,3,7,9]:
            cornersOpen.append(i)

    if len(cornersOpen) > 0:

        move = selectRandom(cornersOpen)

        return move

    if 5 in possible_moves:
        move = 5
        return move



    edgesOpen = []

    for i in possible_moves:
        if i in [2,4,6,8]:
            edgesOpen.append(i)

    if len(edgesOpen) > 0:

        move = selectRandom(edgesOpen)

        return move

    return move



def selectRandom(L):
    ln = len(L)
    r = random.randrange(0 , ln)
    return L[r]


def main():

    print_board(board)

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

main()