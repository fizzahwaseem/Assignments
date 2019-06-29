# Python program to get a string which is n (non-negative integer) copies of a given string
_string = input("Enter your favorite quote: ")
n = int(input("How many time you want it to be displayed? "))
for i in range (0, n):
    i+=1
    print(i, ".", _string)
