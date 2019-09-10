#Python program to create the multiplication table (from 1 to 10) of a number
n = int(input("Enter a number: "))
for i in range(10):
    i = i + 1
    print( n, "x", i, "=", i * n)