
# 2. Searching Algorithms
# Linear Search

# python

def linear_search(arr, target):
    for index, value in enumerate(arr):
        if value == target:
            return index
    return -1

# Example usage
arr = [10, 20, 30, 40, 50]
result = linear_search(arr, 30)
print(result)  # Output: 2

# Binary Search

# python

def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = arr[mid]
        
        if guess == target:
            return mid
        if guess > target:
            high = mid - 1
        else:
            low = mid + 1
    
    return -1

# Example usage
arr = [10, 20, 30, 40, 50]
result = binary_search(arr, 30)
print(result)  # Output: 2











# 2. Searching Algorithms
# Linear Search

# python

# def linear_search(arr, target):
#     for index, value in enumerate(arr):
#         if value == target:
#             return index
#     return -1

# # Example usage
# arr = [10, 20, 30, 40, 50]
# result = linear_search(arr, 30)
# print(result)  # Output: 2

# Binary Search

# python

# def binary_search(arr, target):
#     low = 0
#     high = len(arr) - 1

#     while low <= high:
#         mid = (low + high) // 2
#         guess = arr[mid]
        
#         if guess == target:
#             return mid
#         if guess > target:
#             high = mid - 1
#         else:
#             low = mid + 1
    
#     return -1

# # Example usage
# arr = [10, 20, 30, 40, 50]
# result = binary_search(arr, 30)
# print(result)  # Output: 2
