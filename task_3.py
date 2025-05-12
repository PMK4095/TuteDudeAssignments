#Task 3: Check if a Number is Even or Odd
number=abs(int(input("Enter a number :")))
result = number%2
if result==0:
    print(number,"is an even number.")
else:
    print(number,'is an odd number.')