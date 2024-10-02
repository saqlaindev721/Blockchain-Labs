
# 7. Binary Search Trees (BST)

# Description: A BST is a tree where each node has at most two children, and the left child is less than the parent node, while the right child is greater.

# Example:

# python

class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = BSTNode(value)
        else:
            self._insert(self.root, value)

    def _insert(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = BSTNode(value)
            else:
                self._insert(node.left, value)
        else:
            if node.right is None:
                node.right = BSTNode(value)
            else:
                self._insert(node.right, value)

    def inorder_traversal(self):
        def _inorder(node):
            if node is not None:
                _inorder(node.left)
                print(node.value, end=' ')
                _inorder(node.right)

        _inorder(self.root)
        print()

# Example usage
bst = BST()
bst.insert(5)
bst.insert(3)
bst.insert(7)
bst.inorder_traversal()  # Output: 3 5 7





















# 7. Binary Search Trees (BST)

# Description: A BST is a tree where each node has at most two children, and the left child is less than the parent node, while the right child is greater.

# Example:

# python

# class BSTNode:
#     def __init__(self, value):
#         self.value = value
#         self.left = None
#         self.right = None

# class BST:
#     def __init__(self):
#         self.root = None

#     def insert(self, value):
#         if self.root is None:
#             self.root = BSTNode(value)
#         else:
#             self._insert(self.root, value)

#     def _insert(self, node, value):
#         if value < node.value:
#             if node.left is None:
#                 node.left = BSTNode(value)
#             else:
#                 self._insert(node.left, value)
#         else:
#             if node.right is None:
#                 node.right = BSTNode(value)
#             else:
#                 self._insert(node.right, value)

#     def inorder_traversal(self):
#         def _inorder(node):
#             if node is not None:
#                 _inorder(node.left)
#                 print(node.value, end=' ')
#                 _inorder(node.right)

#         _inorder(self.root)
#         print()

# # Example usage
# bst = BST()
# bst.insert(5)
# bst.insert(3)
# bst.insert(7)
# bst.inorder_traversal()  # Output: 3 5 7
