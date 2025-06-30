from itertools import permutations

def solve_cryptarithmetic():
    # Unique characters in the problem
    letters = 'SENDMORY'
    
    # Ensure letters are unique
    assert len(letters) == len(set(letters))

    # Try all permutations of digits for the 8 unique letters
    for perm in permutations(range(10), len(letters)):
        mapping = dict(zip(letters, perm))

        # Leading characters should not be zero
        if mapping['S'] == 0 or mapping['M'] == 0:
            continue

        # Construct the actual numbers from the mapping
        send = 1000 * mapping['S'] + 100 * mapping['E'] + 10 * mapping['N'] + mapping['D']
        more = 1000 * mapping['M'] + 100 * mapping['O'] + 10 * mapping['R'] + mapping['E']
        money = 10000 * mapping['M'] + 1000 * mapping['O'] + 100 * mapping['N'] + 10 * mapping['E'] + mapping['Y']

        if send + more == money:
            print(f"SEND + MORE = MONEY")
            print(f"{send} + {more} = {money}")
            print("Mapping:")
            for k, v in mapping.items():
                print(f"{k} = {v}")
            return

    print("No solution found.")

# Run the solver
solve_cryptarithmetic()
