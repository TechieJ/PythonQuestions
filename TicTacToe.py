from random import randrange
from time import sleep

def display_board(board):
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.
    for row in board:
        print("+-------+-------+-------+")
        print("|       |       |       |")
        print("|   {0}   |   {1}   |   {2}   |".format(row[0],row[1],row[2]))
        print("|       |       |       |")
    print("+-------+-------+-------+")

def enter_move(board):
    # The function accepts the board's current status, asks the user about their move, 
    # checks the input, and updates the board according to the user's decision.
    while 1:
        user_os = int(input("Hey User! Make your move. Make sure to enter between 1 and 9: "))
        if user_os > 0 and user_os < 10:
            if moves[user_os] not in make_list_of_free_fields(board):
                print("The square is already occupied. Incorrect move. Please try again...")
            else:
                break
        else:
            print('Move should be between 1 and 9. Please try again...')

    board[moves[user_os][0]][moves[user_os][1]] = 'O'
    victory_for(board, 'O')
def make_list_of_free_fields(board):
    # The function browses the board and builds a list of all the free squares; 
    # the list consists of tuples, while each tuple is a pair of row and column numbers.  
    free=[]
    for row in range(3):
        for col in range(3):
            if board[row][col] not in ('X','O'):
                free.append((row,col))
    return free

def victory_for(board, sign):
    # The function analyzes the board's status in order to check if 
    # the player using 'O's or 'X's has won the game
    winner={'X': 'Computer', 'O': 'User'}
    won = False

    if board[0][0] ==  board[1][1] == board[2][2] == sign:
        print(winner[sign], ' WON the game !!!')
        won = True

    if board[2][0] ==  board[1][1] == board[0][2] == sign:
        print(winner[sign], ' WON the game')
        won = True

    for i in range(3):
        if board[0][i] ==  board[1][i] == board[2][i] == sign:
            print(winner[sign], ' WON the game')
            won = True
        
        if board[i][0] ==  board[i][1] == board[i][2] == sign:
            print(winner[sign], ' WON the game')
            won = True

    if len(make_list_of_free_fields(board)) == 0 and won == False:
        print('Game tie')
        won = True

    if won:
        print("Results:")
        display_board(board)
        exit(0)

    print('Continue playing the game...')

def draw_move(board):
    # The function draws the computer's move and updates the board.
    print("Computer move...")
    print("Thinking...")
    sleep(1)
    if len(make_list_of_free_fields(board)) == 9:
            print('Computer selected: 5')
            board[1][1] = 'X'
            return
    
    while 1:
        comp_xs = randrange(9)
        print('Computer selected: ',comp_xs+1)
        if moves[comp_xs+1] not in make_list_of_free_fields(board):
            print("The square is already occupied. Incorrect move. Please try again...")
        else:
            break
    board[moves[comp_xs+1][0]][moves[comp_xs+1][1]] = 'X'
    victory_for(board, 'X')

board = [[1,2,3],[4,5,6],[7,8,9]]
moves = {1:(0,0),2:(0,1),3:(0,2),4:(1,0),5:(1,1),6:(1,2),7:(2,0),8:(2,1),9:(2,2)}
while 1:
    draw_move(board)
    display_board(board)
    #print('Free slots: ', make_list_of_free_fields(board))
    enter_move(board)
    display_board(board)