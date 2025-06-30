from collections import deque

# Goal configuration
goal = '123456780'  # 0 represents the blank space

# Directions to move (up, down, left, right)
moves = {
    0: [1, 3],          # from index 0, can move to 1 (right), 3 (down)
    1: [0, 2, 4],
    2: [1, 5],
    3: [0, 4, 6],
    4: [1, 3, 5, 7],
    5: [2, 4, 8],
    6: [3, 7],
    7: [4, 6, 8],
    8: [5, 7]
}

def bfs(start):
    visited = set()
    queue = deque()
    queue.append((start, []))

    while queue:
        state, path = queue.popleft()
        if state == goal:
            return path + [state]

        visited.add(state)
        zero_pos = state.index('0')

        for move_pos in moves[zero_pos]:
            new_state = list(state)
            new_state[zero_pos], new_state[move_pos] = new_state[move_pos], new_state[zero_pos]
            new_state_str = ''.join(new_state)
            if new_state_str not in visited:
                queue.append((new_state_str, path + [state]))

    return None

# Example initial configuration
start = '123405678'  # represents:
# 1 2 3
# 4 0 5
# 6 7 8

solution = bfs(start)

# Print the solution
if solution:
    print("Solution found in", len(solution) - 1, "moves:")
    for state in solution:
        for i in range(0, 9, 3):
            print(state[i:i+3])
        print("---")
else:
    print("No solution found.")
