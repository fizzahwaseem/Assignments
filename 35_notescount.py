#Python program to find the number of notes (Sample of notes: 10, 20, 50, 100, 500, and 1000 ) against an given amount
total_amount = int(input("Enter total number of ammount: "))
th = total_amount // 1000
a = total_amount % 1000
fiv = a // 500
b = a % 500
hun = b // 100
c = b % 100
fif = c // 50
d = c % 50
twe = d // 20
e = d % 20
ten = e // 10
print("Number of notes \nThousand rupee: ", th, "\nFive Hundred Rupee ", fiv, "\nHundred Rupee", hun, "\nFifty Rupee ", fif, "\nTwenty Rupee ", twe, "\nTen Rupee", ten)