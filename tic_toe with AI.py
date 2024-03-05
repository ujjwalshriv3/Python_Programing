import random
def print_board(board):
    for i in range(3):
        row = [board[i*3 + j] for j in range(3)]
        print(' | '.join(row))
        if i < 2:
            print('-' * 9)
def check_winner(board, player):
    for i in range(3):
        if all(board[i*3 + j] == player for j in range(3)):
            return True
    for i in range(3):
        if all(board[i + j*3] == player for j in range(3)):
            return True
    if board[0] == player and board[4] == player and board[8] == player:
        return True
    if board[2] == player and board[4] == player and board[6] == player:
        return True
    return False
def make_move(board, player, position):
    if 0 <= position < 9 and board[position] == ' ':
        board[position] = player
        return True
    else:
        return False
def get_computer_move(board):
    available_moves = [i for i in range(9) if board[i] == ' ']
    return random.choice(available_moves)
def play_game():
    board = [' ' for _ in range(9)]
    current_player = 'X'
    while True:
        print_board(board)
        if current_player == 'X':
            position = int(input('Your turn player X\nEnter position (0-8): '))
            if make_move(board, current_player, position):
                if check_winner(board, current_player):
                    print_board(board)
                    print('Congratulations! You won!')
                    break
                else:
                    current_player = 'O'
            else:
                print('That space are already fill ! .try another ')
        else:
            position = get_computer_move(board)
            print(f"AI's turn  {position}")
            if make_move(board, current_player, position):
                if check_winner(board, current_player):
                    print_board(board)
                    print('Sorry! AI won!')
                    break
                else:
                    current_player = 'X'
            else:
                print('Invalid move by the AI Something went wrong.')
        if all(cell != ' ' for cell in board):
            print_board(board)
            print("It's a tie!")
            break
play_game()