def show_game(board):
    print()
    for row in range(3):
        print(*board[row], sep=" | ")
        print("---------")

def check_win(board):
    if board[0][0] == board[0][1] and board[0][0] == board[0][2]:
        return get_winner(board[0][0])
    elif board[1][0] == board[1][1] and board[1][0] == board[1][2]:
        return get_winner(board[1][0])
    elif board[2][0] == board[2][1] and board[2][0] == board[2][2]:
        return get_winner(board[2][0])
    elif board[0][0] == board[1][0] and board[0][0] == board[2][0]:
        return get_winner(board[0][0])
    elif board[0][1] == board[1][1] and board[0][1] == board[2][1]:
        return get_winner(board[0][1])
    elif board[0][2] == board[1][2] and board[0][2] == board[2][2]:
        return get_winner(board[0][2])
    elif board[0][0] == board[1][1] and board[0][0] == board[2][2]:
        return get_winner(board[0][0])
    elif board[0][2] == board[1][1] and board[0][2] == board[2][0]:
        return get_winner(board[0][2])
    else:
        return 0

def get_winner(cell):
    if cell == "X":
        return 1
    else:
        return -1

def check_play(move, board):
    try:
        move = int(move)
        if move < 1 or move > 9 or type(board[table[move][0]][table[move][1]]) is not int:
            print("Invalid move!\n")
            return False
        return True
    except ValueError:
        print("Invalid move!\n")
        return False
    
def start_game():
    return [[1,2,3],[4,5,6],[7,8,9]]

def change_player(player):
    if player == "X":
        return "O"
    return "X"

def get_better_option(possible_moves, player):
    if player == "X":
        return max(list(possible_moves.values()))
    return min(list(possible_moves.values()))

def minimax(board, player):
    copy_board = list()
    possible_moves = dict()
    for i in range(3):
        copy_board.append(board[i].copy())
        for j in range(3):
            if type(board[i][j]) is int:
                possible_moves[board[i][j]] = 0
    
    for move in possible_moves:
        copy_board[table[move][0]][table[move][1]] = player
        winner = check_win(copy_board)
        if winner == 0 and len(possible_moves) > 1:
            options = minimax(copy_board, change_player(player))
            possible_moves[move] = get_better_option(options, player)
        else:
            possible_moves[move] = winner

        copy_board[table[move][0]][table[move][1]] = move

    return possible_moves
    
table = {1: [0, 0], 2: [0, 1], 3: [0, 2], 4: [1, 0], 5: [1, 1], 6: [1, 2], 7: [2, 0], 8: [2, 1], 9: [2, 2]}
curr_player = "X"

while True:
    board = start_game()
    for i in range(9):

        if curr_player == "O":
            options = minimax(board, curr_player)
            move = list(options.keys())[list(options.values()).index(get_better_option(options, curr_player))]
        else:
            print(f"\nYour turn!")
            show_game(board)
            move = input("Make your move: ")
            while not check_play(move, board):
                move = input("Make your move: ")
        
        board[table[int(move)][0]][table[int(move)][1]] = curr_player

        curr_player = change_player(curr_player)

        winner = check_win(board)
        if winner:
            show_game(board)
            if winner == 1:
                print("---------\nX Won!\n---------")
            else:
                print("---------\nO Won!\n---------")
            break

        if i == 8:
            show_game(board)
            print("---------\nDraw!\n---------")

    answer = ""
    while answer != "y" and answer != "n":
        answer = input("Would you like to play again (y/n)? ").lower()
    
    if answer == "n":
        break