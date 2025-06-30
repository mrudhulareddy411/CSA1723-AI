from collections import deque

def bfs(graph, start):
    visited = set()              # To keep track of visited nodes
    queue = deque([start])       # Queue for BFS

    print("BFS Traversal:", end=" ")
    
    while queue:
        vertex = queue.popleft()  # Dequeue a vertex
        if vertex not in visited:
            print(vertex, end=" ")
            visited.add(vertex)   # Mark as visited
            # Add all unvisited adjacent vertices
            for neighbor in graph[vertex]:
                if neighbor not in visited:
                    queue.append(neighbor)

# Example graph as an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

# Run BFS
bfs(graph, 'A')
