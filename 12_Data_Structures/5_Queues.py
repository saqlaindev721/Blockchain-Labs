
from collections import deque

# Create a queue
queue = deque()

# Enqueue elements
queue.append('a')
queue.append('b')
queue.append('c')

# Dequeue elements
print(queue.popleft())  # Output: a
print(queue.popleft())  # Output: b

# Print remaining elements
print(queue)  # Output: deque(['c'])










