#Python program to reverse the digits of a given number and add it to the original, If the sum is not a palindrome repeat this procedure
num = input("Enter a number: ")
num_reverse = num[::-1]
total = int(num) + int(num_reverse)
while True:
    total = str(total)
    if total == total[::-1]:
        print("final palindrome is", total)
        break
    else:
        totalrev = total[::-1]
        totala = int(total) + int(totalrev)
        total = totala
    