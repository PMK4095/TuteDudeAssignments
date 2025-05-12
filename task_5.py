#Calculate factorial using a function

def fact(n):
    if n<2:
        return 1
    else:
        return n*fact(n-1)

x=int(input("Enter a number: "))
value=fact(x)
print("Factorial of", x, "is: ",value)
