# Python program to calculate number of days between two dates
import datetime
date1 = input("Enter Date1: DD/MM/YYYY: ")
date2 = input("Enter Date2: DD/MM/YYYY: ")
date1, month1, year1 = map(int, date1.split('/'))
date2, month2, year2 = map(int, date2.split('/'))
No_of_days = date2 - date1
print("Number of days = ", No_of_days)