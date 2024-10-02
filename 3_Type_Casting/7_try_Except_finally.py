try:
    file = open("example.txt", "r")
    data = file.read()
except FileNotFoundError:
    print("File not found!")
# finally:
    # file.close()  # This will always execute, whether or not an exception occurred



# Try-Except-Finally Block3

# python
# Copy code
# try:
#     file = open("example.txt", "r")
#     data = file.read()
# except FileNotFoundError:
#     print("File not found!")
# finally:
#     file.close()  # This will always execute, whether or not an exception occurred
# Explanation:

# The finally block executes code regardless of whether an exception was raised, often used for cleanup.
