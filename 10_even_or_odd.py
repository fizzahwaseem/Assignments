#Python program to find whether a given number (accept from the user) is even or odd, print out an appropriate message to the user.
number = int(input("Enter a number: "))
if number == 0:
    print("Invalid syntax")
elif number%2 == 0:
    print("Number is even")
else:
    print("number is odd")
 