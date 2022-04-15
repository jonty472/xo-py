import random

print(random.randrange(1,10)) 

moves = []

def xo_game():
    BOARD = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    
    for game in range(2):
        player_move(move = input(': '))

def update_board(position, turn):
    pass


def player_move(move):
    if move not in moves:
        moves.append(move)
    else:
        print("Position Taken. Restart")
        moves.remove(move)
        return xo_game()
    print(moves)

def bot_move():
    pass

xo_game()


