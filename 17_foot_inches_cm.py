#Python program to convert height (in feet and inches) to centimetres.
feet = float(input("Enter Height in feet: "))
inches = float(input("Enter Height in inches: "))
Height_in_cm = (feet + inches/12) * 30.48
print("Height in centimeter is: ", Height_in_cm)
