# Initialize the board
board = [' ' for _ in range(9)]

# Print the current state of the board
def print_board():
    print()
    for i in range(3):
        print(' ' + board[i*3] + ' | ' + board[i*3+1] + ' | ' + board[i*3+2])
        if i < 2:
            print("---|---|---")
    print()

# Check if a player has won
def check_winner(player):
    win_positions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]              # Diagonals
    ]
    for pos in win_positions:
        if all(board[i] == player for i in pos):
            return True
    return False

# Check if the board is full (draw)
def is_draw():
    return ' ' not in board

# Main game loop
def play_game():
    current_player = 'X'
    while True:
        print_board()
        try:
            move = int(input(f"Player {current_player}, enter your move (1-9): ")) - 1
            if board[move] != ' ' or move not in range(9):
                print("Invalid move. Try again.")
                continue
        except:
            print("Invalid input. Please enter a number from 1 to 9.")
            continue

        board[move] = current_player

        if check_winner(current_player):
            print_board()
            print(f"🎉 Player {current_player} wins!")
            break
        elif is_draw():
            print_board()
            print("It's a draw!")
            break

        # Switch player
        current_player = 'O' if current_player == 'X' else 'X'

# Run the game
play_game()
