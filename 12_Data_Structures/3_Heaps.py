
# 3. Heaps

# Description: A heap is a specialized tree-based data structure that satisfies the heap property. A min-heap ensures that the parent node is less than or equal to its children, while a max-heap ensures the opposite.

# Example (Min-Heap using heapq module):

# python

import heapq

# Create a heap (min-heap by default)
heap = []

# Add elements
heapq.heappush(heap, 3)
heapq.heappush(heap, 1)
heapq.heappush(heap, 2)

# Remove and return the smallest element
print(heapq.heappop(heap))  # Output: 1

# Print the remaining elements
print(heap)  # Output: [2, 3]











# 3. Heaps

# Description: A heap is a specialized tree-based data structure that satisfies the heap property. A min-heap ensures that the parent node is less than or equal to its children, while a max-heap ensures the opposite.

# Example (Min-Heap using heapq module):

# python

# import heapq

# # Create a heap (min-heap by default)
# heap = []

# # Add elements
# heapq.heappush(heap, 3)
# heapq.heappush(heap, 1)
# heapq.heappush(heap, 2)

# # Remove and return the smallest element
# print(heapq.heappop(heap))  # Output: 1

# # Print the remaining elements
# print(heap)  # Output: [2, 3]
