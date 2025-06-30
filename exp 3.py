from collections import deque

def water_jug_problem(jug1_capacity, jug2_capacity, target):
    # To store visited states
    visited = set()
    # Queue for BFS
    queue = deque()
    # Initial state (0, 0)
    queue.append((0, 0))
    
    while queue:
        # Current state
        current_jug1, current_jug2 = queue.popleft()
        
        # If the target is reached
        if current_jug1 == target or current_jug2 == target:
            print(f"Solution found: Jug1 = {current_jug1}, Jug2 = {current_jug2}")
            return True
        
        # If the state is already visited, skip it
        if (current_jug1, current_jug2) in visited:
            continue
        
        # Mark the state as visited
        visited.add((current_jug1, current_jug2))
        
        # Possible actions
        actions = [
            (jug1_capacity, current_jug2),  # Fill Jug1
            (current_jug1, jug2_capacity),  # Fill Jug2
            (0, current_jug2),              # Empty Jug1
            (current_jug1, 0),              # Empty Jug2
            # Pour Jug1 -> Jug2
            (max(0, current_jug1 - (jug2_capacity - current_jug2)), 
             min(jug2_capacity, current_jug1 + current_jug2)),
            # Pour Jug2 -> Jug1
            (min(jug1_capacity, current_jug1 + current_jug2), 
             max(0, current_jug2 - (jug1_capacity - current_jug1)))
        ]
        
        # Add all possible actions to the queue
        for action in actions:
            if action not in visited:
                queue.append(action)
    
    print("No solution found.")
    return False

# Example usage
jug1_capacity = 4
jug2_capacity = 3
target = 2

water_jug_problem(jug1_capacity, jug2_capacity, target)
