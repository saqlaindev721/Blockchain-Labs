
# 2. Linked Lists

# Description: A linked list is a linear data structure where elements are stored in nodes, each pointing to the next node. Python does not have a built-in linked list, so we implement it using classes.

# Example:

# python

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def print_list(self):
        current = self.head
        while current:
            print(current.value)
            current = current.next

# Example usage
ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.print_list()














# 2. Linked Lists

# Description: A linked list is a linear data structure where elements are stored in nodes, each pointing to the next node. Python does not have a built-in linked list, so we implement it using classes.

# Example:

# python

# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.next = None

# class LinkedList:
#     def __init__(self):
#         self.head = None

#     def append(self, value):
#         new_node = Node(value)
#         if not self.head:
#             self.head = new_node
#             return
#         last_node = self.head
#         while last_node.next:
#             last_node = last_node.next
#         last_node.next = new_node

#     def print_list(self):
#         current = self.head
#         while current:
#             print(current.value)
#             current = current.next

# # Example usage
# ll = LinkedList()
# ll.append(1)
# ll.append(2)
# ll.append(3)
# ll.print_list()

