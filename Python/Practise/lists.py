Students = ["Harry", "Ron", "Hermione"]

# Printing students Indivisually
print(Students[0])
print(Students[1])
print(Students[2])

print()

# all students using for loops
for student in Students:
    print(student)
    
print()

for i in range(len(Students)):
    print(i+1, Students[i]) # Indexing students starting with 1

print(Students)
