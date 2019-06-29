#Python program to calculate body mass index. 
weight = int(input("Enter your weight in kg: "))
ft, inch = map(int, (input("Enter yor height in foot inches seperated by space : ")).split("."))
height_in_meter = (ft + inch/12) * 0.3048
BMI = weight / (height_in_meter ** 2)
if BMI < 18.5:
    print("Your BMI is: ", BMI, "You're underweight")
elif 18.5 < BMI < 25:
    print("Your BMI is: ", BMI, "which is normal")
elif 25 < BMI < 30:
    print("Your BMI is: ", BMI, "You're overweight")
else:
    print("Your BMI is: ", BMI, "considered as obese")
