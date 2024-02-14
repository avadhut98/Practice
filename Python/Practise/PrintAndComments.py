# {#} is used for single line comment.

'''
this is multi-line comment.
'''

"""
This is Also multi-line comment.
"""

# Print function
# print(*object, sep = " ", end="\n")

print("Hello, World!")

# Input function

# Taking Name as input from user
name = input("What's your Name: ")

# Remove spaces from string or trim 
trimedname = name.strip()
cap = name.capitalize()
titiledname = name.title()

name = name.strip().title()

# Splitting String
first, last = name.split(' ')
print("Hello, " + first)


# Printing ' or "
print("Hello 'Friend'")
print('Hello "Friend"')


# Greeting User

# Strings concat using "+"
print("Hello, " + name)

# same output
print("Hello, ", end = "")
print(name)

# same output
print("Hello,", name)





