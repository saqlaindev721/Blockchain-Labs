def check_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    return age

try:
    age = check_age(-1)
except ValueError as e:
    print(e)  # Output: Age cannot be negative



# --------------------------------------------
# Raising Exceptions

# python
# Copy code
# def check_age(age):
#     if age < 0:
#         raise ValueError("Age cannot be negative")
#     return age

# try:
#     age = check_age(-1)
# except ValueError as e:
#     print(e)  # Output: Age cannot be negative
# Explanation:

# raise is used to throw an exception intentionally.
# ValueError is raised if the condition is met.
