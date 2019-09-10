#Python program to compute the greatest common divisor (GCD) of two positive integers.
print('To find GCD enter ')
num1 = int(input('number 1 : '))
num2 = int(input('number 2 : '))
if num1 > num2:
        greater = num1
else:
        greater = num2
for i in range(1, greater+1):
    if((num1 % i == 0) and (num2 % i == 0)):
        gcd = i
print('The gcd of' , num1 , 'and' , num2 , 'is' , gcd)