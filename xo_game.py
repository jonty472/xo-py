print("\n"
     "1 | 2 | 3\n"
     "--+---+--\n"
     "4 | 5 | 6\n"
     "--+---+--\n"
     "7 | 8 | 9"
    "\n")

def xo_game():
    """
    Input a board position from 1-9 to mark position of XO.
    Returns the XO board with summary of move(s)
    """

    X_moves = []
    O_moves = []

    moves = []
    moveCount = 0
    board = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    # Game turns prompt and conditional rules based on valid move
    for game in range(9):
        board_position = int(input(': '))
        moves.append(board_position)

        if moveCount%2 == 0:
            moveCount+=1
            X_moves.append(board_position)
            board[int(board_position)] = 'X'
            #print('X_positions: ', X_positions)
        else:
            moveCount+=1
            O_moves.append(board_position)
            board[int(board_position)] = 'O'
            #print('O_positions: ', O_positions)


        # Update board
        print("\n{} | {} | {}\n--+---+--\n{} | {} | {}\n--+---+--\n{} | {} | {}\n".format(
                                                board[1],board[2],board[3],
                                                board[4],board[5],board[6],
                                                board[7],board[8],board[9],)) 
                                                

        # if board position has been taken already game ends
        for move in reversed(moves):
            if moves.count(move) > 1:
                moves.remove(move)
                return print("Position already taken. Start again!")

        # Win Conditions
            #Row Win Conditions 123, 456, and 789
        if int(1) in X_moves and int(2) in X_moves and int(3) in X_moves or int(4) in X_moves and int(5) in X_moves and int(6) in X_moves or int(7) in X_moves and int(8) in X_moves and int(9) in X_moves:
            return print("X Wins")

        elif int(1) in O_moves and int(2) in O_moves and int(3) in O_moves or int(4) in O_moves and int(5) in O_moves and int(6) in O_moves or int(7) in O_moves and int(8) in O_moves and int(9) in O_moves:
            return print('O Wins')
            
            #Column Win Condtions 147, 258, 369
        if int(1) in X_moves and int(4) in X_moves and int(7) in X_moves or int(2) in X_moves and int(5) in X_moves and int(8) in X_moves or int(3) in X_moves and int(6) in X_moves and int(9) in X_moves:
            return print("X Wins")

        elif int(1) in O_moves and int(4) in O_moves and int(7) in O_moves or int(2) in O_moves and int(5) in O_moves and int(8) in O_moves or int(3) in O_moves and int(6) in O_moves and int(9) in O_moves:
            return print("O Wins")
        
        elif moveCount >= 9:
            return print('Draw')

    print('All moves: ',moves)
    print('X_positions: ', X_moves)
    print('O_positions: ', O_moves) 


xo_game()

