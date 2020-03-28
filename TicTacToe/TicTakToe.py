from TikTakToeFunctions import display_board, player_input, place_marker, win_check, choose_first, space_check, full_board_check, player_choice, replay

print('Welcome to Tic Tac Toe!')

playerTup = player_input()

p1Turn = choose_first()
print('\n' + p1Turn + " WILL GO FIRST!")
choice = input('Are you ready to play? Enter Yes or No. ')
boardList = ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ]

while choice.lower() == 'yes':

    # Set the game up here
    #pass

    while not(full_board_check(boardList)):
        #Player 1 Turn
        if p1Turn == "Player 1":
            display_board(boardList)
            print(p1Turn)
            pos = player_choice(boardList)
            place_marker(boardList, playerTup[0], pos)
            
            p1Turn = "Player 2"
            if win_check(boardList, playerTup[0]):
                display_board(boardList)
                print("Congratulations! Player 1 wins!")
                break
            
        # Player2's turn.
        else:
            display_board(boardList)
            print(p1Turn)
            pos = player_choice(boardList)
            place_marker(boardList, playerTup[1], pos)
            
            p1Turn = "Player 1"
            if win_check(boardList, playerTup[1]):
                display_board(boardList)
                print("Congratulations! Player 2 wins!")
                break
        
    else:
        display_board(boardList)
        print("Game Over! No one wins... ")
            #pass    
    if not replay():
        break