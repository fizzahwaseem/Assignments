#program to check whether given input is palindrome or not
string = input("Enter a word: ")
string = string.lower()
if string == string[::-1]:
    print("This word is a palindrome")
else:
    print("This is not a palindrome")