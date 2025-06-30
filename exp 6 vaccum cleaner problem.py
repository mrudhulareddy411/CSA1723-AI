import random

# Define environment with two locations: A and B
environment = {
    'A': random.choice(['Dirty', 'Clean']),
    'B': random.choice(['Dirty', 'Clean'])
}

# Initial position of vacuum
vacuum_location = random.choice(['A', 'B'])

def vacuum_agent(location, environment):
    steps = []
    while environment['A'] == 'Dirty' or environment['B'] == 'Dirty':
        current_status = environment[location]
        steps.append(f"Vacuum at {location}, Room is {current_status}")
        
        if current_status == 'Dirty':
            environment[location] = 'Clean'
            steps.append(f">>> Cleaned Room {location}")
        else:
            # Move to the other room
            location = 'B' if location == 'A' else 'A'
            steps.append(f">>> Moved to Room {location}")

    steps.append("Both rooms are clean!")
    return steps

# Run the agent
print("Initial Environment:")
print(environment)
print(f"Vacuum starts at: {vacuum_location}")
result = vacuum_agent(vacuum_location, environment)

print("\nSteps Taken:")
for step in result:
    print(step)

print("\nFinal Environment State:")
print(environment)
