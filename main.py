"""
Plan -
players input for position wanted
- for loop
    input
    print(input)
    update board

setup game board
assign board positions nums


Win combinations 
-Evalute win conditions by board position nums e.g. 012, 048, 642, 036 etc.
two seperate array for X and O board positions if any win combo in array (even if 0412 in array. filter for win combos)
"""
print("\n"
     "0 | 1 | 2\n"
     "--+---+--\n"
     "3 | 4 | 5\n"
     "--+---+--\n"
     "6 | 7 | 8"
    "\n")

def XO_Game():
    """
    Input a board position from 0-8 to mark position of XO.
    Returns the XO board with summary of move(s)
    """
    moves = []
    board = ["0", "1", "2", "3", "4", "5"]
    # Game turns prompt and conditional rules based on valid move
    for game in range(5):
        board_position = int(input(': '))
        moves.append(board_position)
        
        # Update board
        board[int(board_position)] = 'X'
        print("\n{} | {} | {}\n--+---+--\n{} | {} | {}\n".format(
                                                board[0],board[1],board[2],
                                                board[3],board[4],board[5],)) 
                                                
        #make a .format for loop to input board lst on board e.g. {i} 

        # Check if board loc has been taken already
        for move in reversed(moves):
            if moves.count(move) > 1:
                moves.remove(move)
                return print("Position already taken. Try another move: ")
        
        # Win Conditions
        if int(0) in moves and int(1) in moves and int(2) in moves:
            return print("Win")
    print(moves)




    """
     X_positions = []

    O_positions = []

    # Determine Turns and storing board_loc for win combos
    for game in range(6):
        board_position = int(input(': '))
        if move_count%2 == 0:
            move_count+=1
            X_positions.append(board_position)
            #print('X_positions: ', X_positions)
        elif move_count%2 == 1:
            move_count+=1
            O_positions.append(board_position)
            #print('O_positions: ', O_positions)
    print('X_positions: ', X_positions)
    print('O_positions: ', O_positions)

    # Update board
    if board_position <= int(2):
        row1 = ("0 | 1 | 2\n").replace(str(board_position), 'X')
        return (row1)
    """
XO_Game()