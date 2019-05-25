# program to check if a number is positive, negative or zero
number = float(input("Enter a number: "))
if number > 0:
    print("Number is positive")
elif number == 0:
    print("Number is zero")
elif number < 0:
    print("Number is negative")
else:
    print("Invalid syntax")