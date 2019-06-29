#Python program to convert all units of time into seconds.
hour = int(input("Enter time in hours: "))
minute = int(input("Enter time in minutes: "))
t = (hour * 60 * 60) + (minute * 60)
print("Total time in seconds is: ", t)