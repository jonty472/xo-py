"""
Game win conditions would have been too long and not pratical, so i'm refactoring
this project with creating a game board based on a 2d array. This will be done in
another .py file

"""

"""
Win combinations 
-Evalute win conditions by board position nums e.g. 012, 048, 642, 036 etc.
two seperate array for X and O board positions if any win combo in array (even if 0412 in array. filter for win combos)
"""
print("\n"
     "1 | 2 | 3\n"
     "--+---+--\n"
     "4 | 5 | 6\n"
     "--+---+--\n"
     "7 | 8 | 9"
    "\n")

def XO_Game():
    """
    Input a board position from 1-9 to mark position of XO.
    Returns the XO board with summary of move(s)
    """

    X_positions = []
    O_positions = []

    moves = []
    moveCount = 0
    board = ["0", "1", "2", "3", "4", "5", "6"]
    # Game turns prompt and conditional rules based on valid move
    for game in range(6):
        board_position = int(input(': '))
        moves.append(board_position)

        if moveCount%2 == 0:
            moveCount+=1
            X_positions.append(board_position)
            board[int(board_position)] = 'X'
            #print('X_positions: ', X_positions)
        else:
            moveCount+=1
            O_positions.append(board_position)
            board[int(board_position)] = 'O'
            #print('O_positions: ', O_positions)


        # Update board
        print("\n{} | {} | {}\n--+---+--\n{} | {} | {}\n".format(
                                                board[1],board[2],board[3],
                                                board[4],board[5],board[6],)) 
                                                
        #make a .format for loop to input board lst on board e.g. {i} 

        # if board position has been taken already game ends
        for move in reversed(moves):
            if moves.count(move) > 1:
                moves.remove(move)
                return print("Position already taken. Start again!")

        # Win Conditions (if i list out all win cons, code would be too long
        # and impratical. need a different method for checking)
        if int(1) in X_positions and int(2) in X_positions and int(3) in X_positions:
            return print("X Wins")
        elif int(1) in O_positions and int(2) in O_positions and int(3) in O_positions:
            return print("0 Wins")

        #print(moveCount)
    print('All moves: ',moves)
    print('X_positions: ', X_positions)
    print('O_positions: ', O_positions) 


XO_Game()