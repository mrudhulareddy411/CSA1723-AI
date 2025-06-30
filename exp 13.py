def winner(board, player):
    wins = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
    return any(board[i]==board[j]==board[k]==player for i,j,k in wins)

def minimax(board, is_max):
    if winner(board, "O"): return 1
    if winner(board, "X"): return -1
    if " " not in board: return 0

    scores = []
    for i in range(9):
        if board[i] == " ":
            board[i] = "O" if is_max else "X"
            scores.append(minimax(board, not is_max))
            board[i] = " "
    return max(scores) if is_max else min(scores)

def best_move(board):
    best = -2
    move = -1
    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(board, False)
            board[i] = " "
            if score > best:
                best = score
                move = i
    return move

# Example use:
board = ["X", "O", "X",
         " ", "O", " ",
         " ", " ", "X"]

move = best_move(board)
print("AI should move at:", move)
