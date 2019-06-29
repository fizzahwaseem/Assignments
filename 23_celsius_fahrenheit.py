#Python program to convert temperatures to and from Celsius, Fahrenheit
#T_F = float(input("Enter temperature in fehrenheit"))
#T_C = float(input("Enter temperature in Celsius"))
choice = input("Press 1 for Celsius to Fehrenheit Conversion  \nPress 2 for Fehrenheit to Celsius Conversion \n")
temp = float(input("Enter Temperature: "))
if choice == "1":
    f = 1.8 * temp + 32
    print("Temperature in Fehrenheit is: ", f)
elif choice == "2":
    c = (temp - 32) / 1.8
    print("Temperature in Celsius is: ", c)