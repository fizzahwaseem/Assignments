# Python function to check whether a number is completely divisible by another number. Accept two integer values form the user
number1 = int(input("Enter a Number: "))
number2 = int(input("Enter another Number: "))
if number1%number2 == 0:
    print("Completely divisible")
else:
    print("Not completey divisible")