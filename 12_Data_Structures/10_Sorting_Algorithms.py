
# 9. Sorting Algorithms
# Bubble Sort

# python

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Example usage
arr = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(arr)
print(arr)  # Output: [11, 12, 22, 25, 34, 64, 90]

# Quick Sort

# python

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

# Example usage
arr = [3, 6, 8, 10, 1, 2, 1]
print(quick_sort(arr))  # Output: [1, 1, 2, 3, 6, 8, 10]














# 9. Sorting Algorithms
# Bubble Sort

# python

# def bubble_sort(arr):
#     n = len(arr)
#     for i in range(n):
#         for j in range(0, n-i-1):
#             if arr[j] > arr[j+1]:
#                 arr[j], arr[j+1] = arr[j+1], arr[j]

# # Example usage
# arr = [64, 34, 25, 12, 22, 11, 90]
# bubble_sort(arr)
# print(arr)  # Output: [11, 12, 22, 25, 34, 64, 90]

# Quick Sort

# python

# def quick_sort(arr):
#     if len(arr) <= 1:
#         return arr
#     pivot = arr[len(arr) // 2]
#     left = [x for x in arr if x < pivot]
#     middle = [x for x in arr if x == pivot]
#     right = [x for x in arr if x > pivot]
#     return quick_sort(left) + middle + quick_sort(right)

# # Example usage
# arr = [3, 6, 8, 10, 1, 2, 1]
# print(quick_sort(arr))  # Output: [1, 1, 2, 3, 6, 8, 10]
