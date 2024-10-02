# Create a queue
queue = deque(["first", "second"])

# Enqueue
queue.append("third")

# Dequeue
item = queue.popleft()

print(item)   # Output: first
print(queue)  # Output: deque(['second', 'third'])




# 5. Queues

#     Description: FIFO (First In, First Out) collection. Can be implemented using lists or collections.deque.
#     Operations: Enqueue, dequeue.

# python

# from collections import deque

# # Create a queue
# queue = deque(["first", "second"])

# # Enqueue
# queue.append("third")

# # Dequeue
# item = queue.popleft()

# print(item)   # Output: first
# print(queue)  # Output: deque(['second', 'third'])
