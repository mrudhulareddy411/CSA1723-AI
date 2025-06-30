def print_board(board):
    """Function to print the chessboard configuration."""
    for row in board:
        print(" ".join("Q" if col else "." for col in row))
    print()

def is_safe(board, row, col):
    """Check if it's safe to place a queen at board[row][col]."""
    # Check the column
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check the left diagonal
    for i, j in zip(range(row-1, -1, -1), range(col-1, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check the right diagonal
    for i, j in zip(range(row-1, -1, -1), range(col+1, len(board))):
        if board[i][j] == 1:
            return False

    return True

def solve_8_queens(board, row):
    """Use backtracking to solve the 8 Queens problem."""
    # Base case: If all queens are placed
    if row == len(board):
        print_board(board)
        return True

    # Try placing a queen in all columns of the current row
    for col in range(len(board)):
        if is_safe(board, row, col):
            board[row][col] = 1  # Place queen
            if solve_8_queens(board, row + 1):
                return True  # If placing queen leads to a solution
            board[row][col] = 0  # Backtrack if placing queen doesn't lead to a solution

    return False  # No solution found

def solve():
    # Initialize the 8x8 chessboard (all positions are 0 initially)
    board = [[0 for _ in range(8)] for _ in range(8)]
    
    if not solve_8_queens(board, 0):
        print("No solution exists.")
    else:
        print("Solution found!")

if __name__ == "__main__":
    solve()
