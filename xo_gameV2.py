import random


def xo_game():
    x_moves = []
    o_moves = []

    move_count = 0
    moves = []
    board = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

    for game in range(3):
        if move_count%2 == 0:
            move_count+=1
            x_move = player_move()
            x_moves.append(x_move)
            board[x_move] = 'X'
            print_board(board)
            moves.append(x_move)

        elif move_count%2 == 1:
            move_count+=1
            #o_move = bot_move()
            o_move = 5
            o_moves.append(o_move)
            board[o_move] = 'O'
            print('BOTS MOVE:')
            print_board(board) 
            moves.append(o_move)

        elif valid_move(moves) == False:
            print('not valid move\nstart again...')
            return xo_game()

    print('x:', x_moves)
    print('o:', o_moves)



def bot_move():
    move = random.randint(1,9)
    return move

def player_move():
    move = int(input(': '))
    return move

def print_board(board):
    return print("\n{} | {} | {}\n--+---+--\n{} | {} | {}\n--+---+--\n{} | {} | {}\n".format(board[1],board[2],board[3],board[4],board[5],board[6],board[7],board[8],board[9],))

def valid_move(moves):
    """
    Valid Move checks if a position on the board is taken.
    Input: all moves
    Returns True if board position not taken. False if board position already
    taken.
    """
    for move in reversed(moves):
        if moves.count(move) > 1:
            return False
        else:
            return True
    

xo_game()