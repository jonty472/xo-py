import random

player_moves = []
bot_moves = []
move_count = 0

def xo_game(move_count):
    board = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    
    # who starts the game: player or bot?
    #turn = whos_turn()
    turn = 'Player'
    print(turn)
    players_piece = None
    bots_piece = None
    if turn == 'Player':
        players_piece = 'X'
        bots_piece = 'O'
    else:
        bots_piece = 'X'
        players_piece = 'O'
    
    print(turn, 'player:',players_piece, 'bot:',bots_piece)

    # control flow for board and moves
    for game in range(2):
        if players_piece == 'X':
            move = int(input(': '))
            board_position = player_move(move)
            if move_count%2 == 0:
                move_count += 1
                player_moves.append(board_position)
                board[int(board_position)] = 'X'
            else:
                move_count += 1
                bot_moves.append(board_position)
                board[int(board_position)] = 'O'

        elif bots_piece == 'X':
            board_position = bot_move()
            if move_count%2 == 0:
                move_count += 1
                bot_moves.append(board_position)
                board[int(board_position)] = 'X'
            else:
                move_count += 1
                player_moves.append(board_position)
                board[int(board_position)] = 'O'
            
            

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
        turn = 'Player'
    elif bot_roll > player_roll:
        turn = 'Bot'
    elif int(player_roll) == int(bot_roll):
        print('equal. roll again')
        return whos_turn()

    return turn

def player_move(move):
    if move not in player_moves:
        player_moves.append(move)
    else:
        print("Position Taken. Restart")
        player_moves.remove(move)
        return xo_game()
    #print(moves)

def bot_move():
    move_count = move_count + 1
    move = random.randint(1,9)
    if move not in bot_moves:
        bot_moves.append(move)
    else:
        bot_moves.remove(move)
    
xo_game(move_count)
print('player moves', player_moves)
print('bot moves', bot_moves)


