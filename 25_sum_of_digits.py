#Python program to calculate the sum of the digits in an integer
n = input("Enter a number: ")
sum_of_digits = 0
for i in n:
    sum_of_digits += int(i)
print("sum of digits is ", sum_of_digits)