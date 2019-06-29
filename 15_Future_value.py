#Python program to compute the future value of a specified principal amount, rate of interest, and a number of years
amount = int(input("Enter the principle amount: "))
interest_rate = float(input("Enter interest rate: "))
no_of_years = int(input("Enter number of years: "))
Future_value = amount * ((1 + (interest_rate/100)) ** no_of_years)
print("Future value of principle amount is: ", Future_value)