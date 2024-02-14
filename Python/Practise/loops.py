# Print meow  3 times
print("meow\n" * 3)

print("meow\n" * 3, end = "") # Eliminates extra line of previous solution

print()

for i in [1, 2, 3]:
    print("meow")
    
print()

for i in range(3):
    print("meow")
    
# Taking Conditional Inputs
while True:
    # taking non-negative integer as input
    n = int(input("Enter Value of n = "))
    if n >= 0:
        break

def getPositiveInt():
    while True:
        n = int(input("Enter Integer: "))
        if n > 0:
            break
    return n

getPositiveInt()
        
    