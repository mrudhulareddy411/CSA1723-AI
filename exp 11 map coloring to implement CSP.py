def is_valid(region, color, assignment, neighbors):
    # Check if the current color conflicts with neighboring assignments
    for neighbor in neighbors[region]:
        if neighbor in assignment and assignment[neighbor] == color:
            return False
    return True

def backtrack(assignment, variables, domains, neighbors):
    # If assignment is complete
    if len(assignment) == len(variables):
        return assignment

    # Select unassigned variable
    unassigned = [v for v in variables if v not in assignment]
    var = unassigned[0]

    for color in domains:
        if is_valid(var, color, assignment, neighbors):
            assignment[var] = color
            result = backtrack(assignment, variables, domains, neighbors)
            if result:
                return result
            del assignment[var]  # backtrack

    return None  # No valid color found

def map_coloring_csp():
    # Variables (Regions)
    variables = ['WA', 'NT', 'SA', 'Q', 'NSW', 'V', 'T']

    # Domain (Colors)
    domains = ['Red', 'Green', 'Blue']

    # Adjacency map
    neighbors = {
        'WA': ['NT', 'SA'],
        'NT': ['WA', 'SA', 'Q'],
        'SA': ['WA', 'NT', 'Q', 'NSW', 'V'],
        'Q': ['NT', 'SA', 'NSW'],
        'NSW': ['Q', 'SA', 'V'],
        'V': ['SA', 'NSW'],
        'T': []
    }

    # Empty assignment
    assignment = {}

    # Solve using backtracking
    solution = backtrack(assignment, variables, domains, neighbors)

    if solution:
        print("Map Coloring Solution:")
        for region in sorted(solution):
            print(f"{region}: {solution[region]}")
    else:
        print("No solution found.")

# Run the CSP map coloring solver
map_coloring_csp()
