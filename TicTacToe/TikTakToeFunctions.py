from IPython.display import clear_output
import random

def display_board(board):
    print('\n'*100)
    line1 = f' {board[7]} | {board[8]} | {board[9]} '
    lineFill = '   |   |   '
    hLine = '-----------'
    line2 = f' {board[4]} | {board[5]} | {board[6]} '
    line3 = f' {board[1]} | {board[2]} | {board[3]} '
    print(lineFill)
    print(line1)
    print(lineFill)
    print(hLine)
    print(lineFill)
    print(line2)
    print(lineFill)
    print(hLine)
    print(lineFill)
    print(line3)
    print(lineFill)

def player_input():
    player1 = ''
    while not(player1.upper() == 'O') and not(player1.upper() == 'X'):
        player1 = input('Player 1: Do You Want to be X or O? ').upper()
    
    if player1 == 'X':
        player2 = 'O'
    else:
        player2 = 'X'
    return (player1, player2)

def place_marker(board, marker, position):
    
    board[position] = marker

def win_check(board, mark):
    
    return ((board[7] == board[8] == board[9] == mark) or 
    (board[4] == board[5] == board[6] == mark) or 
    (board[1] == board[2] == board[3] == mark) or 
    (board[7] == board[4] == board[1] == mark) or 
    (board[8] == board[5] == board[2] == mark) or 
    (board[9] == board[6] == board[3] == mark) or 
    (board[7] == board[5] == board[3] == mark) or 
    (board[9] == board[5] == board[1] == mark))


def choose_first():
    if random.randint(1,2) == 1:
        return "Player 1"
    else:
        return "Player 2"
    
def space_check(board, position):
    
    return ' ' == board[position]

def full_board_check(board):
    
    return not(' ' in board)

def player_choice(board):
    choice = int(input("Choose your next Position: (1-9)"))
    if space_check(board, choice):
        return choice
    else:
        print("That space is taken. Try again.")
        return player_choice(board)

def replay():
    
    choice = input("Do you want to play again? Enter Yes or No: ")
    return choice.lower() == "yes"