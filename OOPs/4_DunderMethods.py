
# 4. Dunder Methods

# Description: Dunder methods (short for "double underscore" methods) are special methods with double underscores at the beginning and end of their names. They allow you to define how objects of your class behave with built-in operations and functions.

# Common Dunder Methods:

#     __init__(self, ...): Constructor, initializes object attributes.
#     __str__(self): Defines a human-readable string representation of the object.
#     __repr__(self): Defines an official string representation of the object (useful for debugging).
#     __len__(self): Defines behavior for the len() function.
#     __add__(self, other): Defines behavior for the + operator.
#     __eq__(self, other): Defines behavior for the equality operator ==.

# Example:

# python

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"

    def __repr__(self):
        return f"Rectangle({self.width}, {self.height})"

    def __len__(self):
        return 2 * (self.width + self.height)  # Perimeter

    def __add__(self, other):
        if isinstance(other, Rectangle):
            return Rectangle(self.width + other.width, self.height + other.height)
        return NotImplemented

# Creating objects of Rectangle class
rect1 = Rectangle(4, 5)
rect2 = Rectangle(2, 3)

# Using dunder methods
print(rect1)                # Output: Rectangle(width=4, height=5)
print(repr(rect1))          # Output: Rectangle(4, 5)
print(len(rect1))           # Output: 18 (Perimeter of the rectangle)
rect3 = rect1 + rect2
print(rect3)                # Output: Rectangle(width=6, height=8)

# Summary

#     Classes: Define objects with attributes and methods.
#     Inheritance: Allows new classes to inherit attributes and methods from existing classes.
#     Methods: Functions defined inside classes to operate on objects.
#     Dunder Methods: Special methods that allow objects to interact with built-in Python functions and operators.

# These concepts form the foundation of object-oriented programming in Python, enabling you to create more structured and reusable code.



























# 4. Dunder Methods

# Description: Dunder methods (short for "double underscore" methods) are special methods with double underscores at the beginning and end of their names. They allow you to define how objects of your class behave with built-in operations and functions.

# Common Dunder Methods:

#     __init__(self, ...): Constructor, initializes object attributes.
#     __str__(self): Defines a human-readable string representation of the object.
#     __repr__(self): Defines an official string representation of the object (useful for debugging).
#     __len__(self): Defines behavior for the len() function.
#     __add__(self, other): Defines behavior for the + operator.
#     __eq__(self, other): Defines behavior for the equality operator ==.

# Example:

# python

# class Rectangle:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height

#     def __str__(self):
#         return f"Rectangle(width={self.width}, height={self.height})"

#     def __repr__(self):
#         return f"Rectangle({self.width}, {self.height})"

#     def __len__(self):
#         return 2 * (self.width + self.height)  # Perimeter

#     def __add__(self, other):
#         if isinstance(other, Rectangle):
#             return Rectangle(self.width + other.width, self.height + other.height)
#         return NotImplemented

# # Creating objects of Rectangle class
# rect1 = Rectangle(4, 5)
# rect2 = Rectangle(2, 3)

# # Using dunder methods
# print(rect1)                # Output: Rectangle(width=4, height=5)
# print(repr(rect1))          # Output: Rectangle(4, 5)
# print(len(rect1))           # Output: 18 (Perimeter of the rectangle)
# rect3 = rect1 + rect2
# print(rect3)                # Output: Rectangle(width=6, height=8)

# Summary

#     Classes: Define objects with attributes and methods.
#     Inheritance: Allows new classes to inherit attributes and methods from existing classes.
#     Methods: Functions defined inside classes to operate on objects.
#     Dunder Methods: Special methods that allow objects to interact with built-in Python functions and operators.

# These concepts form the foundation of object-oriented programming in Python, enabling you to create more structured and reusable code.