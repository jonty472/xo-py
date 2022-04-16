import random

moves = []
bot_moves = []

def xo_game():
    BOARD = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    whos_turn()
    for game in range(2):
        if whos_turn() == 'Player':
            player_move(move = input(': '))
        else:
            bot_move()


def update_board(position, turn):
    pass



def whos_turn():
    """
    Rolls a dice to see who begins.

    Returns if XO player or bot starts
    """
    player_roll = random.randrange(1,6)
    bot_roll = random.randrange(1,6)
    if player_roll > bot_roll:
        return 'Player'
    elif bot_roll > player_roll:
        return 'Bot'
    else:
        print('equal. roll again')
        return whos_turn()

def player_move(move):
    if move not in moves:
        moves.append(move)
    else:
        print("Position Taken. Restart")
        moves.remove(move)
        return xo_game()
    #print(moves)

def bot_move():
    move = random.randint(1,9)
    if move not in bot_moves:
        bot_moves.append(move)
    else:
        bot_moves.remove(move)
    
xo_game()
print('player moves', moves)
print('bot moves', bot_moves)


