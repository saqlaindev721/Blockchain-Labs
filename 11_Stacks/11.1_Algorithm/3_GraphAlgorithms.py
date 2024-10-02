# 3. Graph Algorithms
# Breadth-First Search (BFS)

# python

from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    while queue:
        vertex = queue.popleft()
        if vertex not in visited:
            visited.add(vertex)
            queue.extend(graph[vertex] - visited)
    return visited

# Example usage
graph = {
    1: {2, 3},
    2: {1, 4, 5},
    3: {1, 6},
    4: {2},
    5: {2},
    6: {3}
}

print(bfs(graph, 1))  # Output: {1, 2, 3, 4, 5, 6}

# Depth-First Search (DFS)

# python

def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    for next in graph[start] - visited:
        dfs(graph, next, visited)
    return visited

# Example usage
graph = {
    1: {2, 3},
    2: {1, 4, 5},
    3: {1, 6},
    4: {2},
    5: {2},
    6: {3}
}

print(dfs(graph, 1))  # Output: {1, 2, 3, 4, 5, 6}

# These examples cover basic data structures and algorithms commonly used in Python programming. Each data structure and algorithm has its use cases, advantages, and limitations. Understanding these concepts helps in writing efficient and effective code.
# Arrays and Linked Lists
# Heaps, Stacks and Queues
# Hash Tables
# Binary Search Trees
# Recursion













# 3. Graph Algorithms
# Breadth-First Search (BFS)

# python

# from collections import deque

# def bfs(graph, start):
#     visited = set()
#     queue = deque([start])
#     while queue:
#         vertex = queue.popleft()
#         if vertex not in visited:
#             visited.add(vertex)
#             queue.extend(graph[vertex] - visited)
#     return visited

# # Example usage
# graph = {
#     1: {2, 3},
#     2: {1, 4, 5},
#     3: {1, 6},
#     4: {2},
#     5: {2},
#     6: {3}
# }

# print(bfs(graph, 1))  # Output: {1, 2, 3, 4, 5, 6}

# Depth-First Search (DFS)

# python

# def dfs(graph, start, visited=None):
#     if visited is None:
#         visited = set()
#     visited.add(start)
#     for next in graph[start] - visited:
#         dfs(graph, next, visited)
#     return visited

# # Example usage
# graph = {
#     1: {2, 3},
#     2: {1, 4, 5},
#     3: {1, 6},
#     4: {2},
#     5: {2},
#     6: {3}
# }

# print(dfs(graph, 1))  # Output: {1, 2, 3, 4, 5, 6}

# These examples cover basic data structures and algorithms commonly used in Python programming. Each data structure and algorithm has its use cases, advantages, and limitations. Understanding these concepts helps in writing efficient and effective code.
# Arrays and Linked Lists
# Heaps, Stacks and Queues
# Hash Tables
# Binary Search Trees
# Recursion
