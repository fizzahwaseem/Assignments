#python program to sum of the first n positive integers
n = int(input("Enter a number: "))
sum_of_n = 0
for i in range(n + 1):
    sum_of_n += i
print("sum of the first", n, "positive integers = ", sum_of_n)
     