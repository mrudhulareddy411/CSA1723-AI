def minimax(depth, node_index, is_max, values, alpha, beta):
    # Base case: leaf node
    if depth == 3:
        return values[node_index]

    if is_max:
        max_eval = float('-inf')
        for i in range(2):
            val = minimax(depth + 1, node_index * 2 + i, False, values, alpha, beta)
            max_eval = max(max_eval, val)
            alpha = max(alpha, val)
            if beta <= alpha:
                break  # Beta cut-off
        return max_eval
    else:
        min_eval = float('inf')
        for i in range(2):
            val = minimax(depth + 1, node_index * 2 + i, True, values, alpha, beta)
            min_eval = min(min_eval, val)
            beta = min(beta, val)
            if beta <= alpha:
                break  # Alpha cut-off
        return min_eval

# Example game tree (leaf node values)
values = [3, 5, 6, 9, 1, 2, 0, -1]

# Call minimax with initial parameters
result = minimax(0, 0, True, values, float('-inf'), float('inf'))
print("The optimal value is:", result)
