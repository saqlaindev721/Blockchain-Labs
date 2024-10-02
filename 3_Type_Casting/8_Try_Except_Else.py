try:
    num = int(input("Enter a number: "))
except ValueError:
    print("That's not a valid number!")
else:
    print(f"You entered the number {num}")



# Try-Except-Else Block

# python
# Copy code
# try:
#     num = int(input("Enter a number: "))
# except ValueError:
#     print("That's not a valid number!")
# else:
#     print(f"You entered the number {num}")
# Explanation:

# The else block executes if no exceptions are raised in the try block.
