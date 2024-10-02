try:
    result = 10 / 0
except ZeroDivisionError:
    print("You can't divide by zero!")





# Exceptions
# Exceptions are errors that occur during the execution of a program. Python uses a mechanism called exception handling to deal with these errors gracefully.

# Common Exception Handling
# Try-Except Block

# python
# Copy code
# try:
#     result = 10 / 0
# except ZeroDivisionError:
#     print("You can't divide by zero!")
# Explanation:

# The try block contains code that may cause an exception.
# The except block handles the exception if it occurs.
# ZeroDivisionError is caught and handled gracefully.
