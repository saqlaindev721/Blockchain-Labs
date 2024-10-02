
# 2. Inheritance

# Description: Inheritance allows a class (child class) to inherit attributes and methods from another class (parent class). It promotes code reuse and establishes a hierarchical relationship between classes.

# Example:

# python

class Animal:
    def __init__(self, species):
        self.species = species

    def eat(self):
        print("This animal is eating.")

class Cat(Animal):  # Cat inherits from Animal
    def __init__(self, name, age):
        super().__init__('Cat')  # Initialize the parent class
        self.name = name
        self.age = age

    def meow(self):
        print(f"{self.name} is meowing!")

# Creating an object of the Cat class
my_cat = Cat("Whiskers", 2)

# Accessing inherited attributes and methods
print(my_cat.species)  # Output: Cat
my_cat.eat()          # Output: This animal is eating.
my_cat.meow()         # Output: Whiskers is meowing!






















# 2. Inheritance

# Description: Inheritance allows a class (child class) to inherit attributes and methods from another class (parent class). It promotes code reuse and establishes a hierarchical relationship between classes.

# Example:

# python

# class Animal:
#     def __init__(self, species):
#         self.species = species

#     def eat(self):
#         print("This animal is eating.")

# class Cat(Animal):  # Cat inherits from Animal
#     def __init__(self, name, age):
#         super().__init__('Cat')  # Initialize the parent class
#         self.name = name
#         self.age = age

#     def meow(self):
#         print(f"{self.name} is meowing!")

# # Creating an object of the Cat class
# my_cat = Cat("Whiskers", 2)

# # Accessing inherited attributes and methods
# print(my_cat.species)  # Output: Cat
# my_cat.eat()          # Output: This animal is eating.
# my_cat.meow()         # Output: Whiskers is meowing!
