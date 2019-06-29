#Python program to convert the distance (in feet) to inches, yards, and miles. 1 feet = 12 inches, 3 feet = 1 yard, 5280 feet = 1 mile
distance_in_feet = float(input("Enter distance in feet: "))
distance_in_inches = 12 * distance_in_feet
distance_in_yard = (1/3) * distance_in_feet
distance_in_miles = (1/5280) * distance_in_feet
print("Distance in inches is: ", distance_in_inches)
print("Distance in yard is: ", distance_in_yard)
print("Distance in mile is: ", distance_in_miles)