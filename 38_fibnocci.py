#Python program to get the Fibonacci series between 0 to 50
a = 0
b = 1
while b <= 50:
    c = a + b
    a = b
    b = c
    if b <= 50:
        print(b)