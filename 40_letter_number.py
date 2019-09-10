#Python program that accepts a string and calculate the number of digits and letters
string = input("Enter a string: ")
letter = 0
number = 0
string = string.lower()
for i in string:
    if i in "abcdefghijklmnopqrstuvwxyz":
        letter += 1
    elif i in "0123456789":
        number += 1
print("letters", letter, "digits", number)