def hello(to="User"): # User is default here if there is no variable provided
    print("Hello,", to)


# Taking Name as input from user
name = input("What's your Name: ")
name = name.strip().title()

hello(name)
#no variable provided
hello()



# We can use main method to write finctions after the code just like below
def main():
    x = int(input("Enter Value of x = "))
    print("Squre of x is", square(x))

def square(n):
    return n**2 # pow(n,2) or n * n

main()
