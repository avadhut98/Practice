Students = {
    "Harry": "Gryffindor",
    # Harry is 'Key' And Gryffindor is 'Value'
    "Ron": "Gryffindor",
    "Hermoine": "Gryffindor",
    "Draco": "Slytherin"
}

# Prints values
print(Students["Harry"])
print(Students["Draco"])

print()

# Print Keys using for loop
for student in Students:
    print(student)
    
print()

# Printing pairs
for student in Students:
    print(student, Students[student])

print()
print(Students)
