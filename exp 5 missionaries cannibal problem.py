from collections import deque

def is_valid_state(ml, cl, mr, cr):
    # Valid if no group of missionaries is outnumbered
    if (ml < 0 or cl < 0 or mr < 0 or cr < 0):
        return False
    if (ml > 0 and ml < cl):
        return False
    if (mr > 0 and mr < cr):
        return False
    return True

def get_successors(state):
    successors = []
    ml, cl, mr, cr, boat = state
    moves = [(1, 0), (0, 1), (1, 1), (2, 0), (0, 2)]  # Possible moves

    for m, c in moves:
        if boat == 'L':
            new_state = (ml - m, cl - c, mr + m, cr + c, 'R')
        else:
            new_state = (ml + m, cl + c, mr - m, cr - c, 'L')
        
        if is_valid_state(*new_state[:4]):
            successors.append(new_state)
    return successors

def missionaries_and_cannibals():
    initial_state = (3, 3, 0, 0, 'L')
    goal_state = (0, 0, 3, 3, 'R')
    visited = set()
    queue = deque()
    queue.append((initial_state, [initial_state]))

    while queue:
        current_state, path = queue.popleft()
        if current_state in visited:
            continue
        visited.add(current_state)

        if current_state == goal_state:
            print("Solution Path:")
            for step in path:
                print(step)
            return
        for next_state in get_successors(current_state):
            if next_state not in visited:
                queue.append((next_state, path + [next_state]))

    print("No solution found.")

# Run the program
missionaries_and_cannibals()
