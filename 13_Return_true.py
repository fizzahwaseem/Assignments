#Python program that will return true if the two given integer values are equal or their sum or difference is 5
n1 = int(input("Enter an integer: "))
n2 = int(input("Enter another integer: "))
if n1 == n2:
    result = True
elif n1 + n2 == 5:
    result = True
elif n1 - n2 == 5 or n2 - n1 == 5:
    result = True
else:
    result = False
print(result)