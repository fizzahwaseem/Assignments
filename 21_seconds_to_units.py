#Python program to convert seconds to day, hour, minutes and seconds
seconds = int(input("Enter time in seconds: "))
day = seconds // 86400
s1 = seconds % 86400
hour = s1 // 3600
s2 = s1 % 3600
minute = s2 // 60
s3 = s2 % 60
second = s3
print(day, "days, ", hour, "hours, ", minute, "minutes and", second, "seconds")
print("day:hour:minute:second = ", day, ":", hour, ":", minute, ":", second)