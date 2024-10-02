
# 3. Methods

# Description: Methods are functions defined inside a class that operate on instances of the class. They can access and modify object attributes.

# Example:

# python

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."

    def have_birthday(self):
        self.age += 1
        print(f"Happy Birthday, {self.name}! You are now {self.age}.")

# Creating an object of the Person class
person = Person("Alice", 30)

# Calling methods
print(person.greet())        # Output: Hello, my name is Alice and I am 30 years old.
person.have_birthday()      # Output: Happy Birthday, Alice! You are now 31.




























# 3. Methods

# Description: Methods are functions defined inside a class that operate on instances of the class. They can access and modify object attributes.

# Example:

# python

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def greet(self):
#         return f"Hello, my name is {self.name} and I am {self.age} years old."

#     def have_birthday(self):
#         self.age += 1
#         print(f"Happy Birthday, {self.name}! You are now {self.age}.")

# # Creating an object of the Person class
# person = Person("Alice", 30)

# # Calling methods
# print(person.greet())        # Output: Hello, my name is Alice and I am 30 years old.
# person.have_birthday()      # Output: Happy Birthday, Alice! You are now 31.
