#Python program to calculate the hypotenuse of a right angled triangle
from math import sqrt
a = float(input("Enter magnitude of perpendicular: "))
b = float(input("Enter magnitude of base: "))
c = sqrt(a**2 + b**2)
print("Hypotenuse is: ", c)