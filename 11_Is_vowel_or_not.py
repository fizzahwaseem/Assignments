# Python program to test whether a passed letter is a vowel or not
letter = input("Enter a letter: ")
_vowels = ["a", "e", "i", "o", "u"]
letter = letter.lower()
if letter in _vowels:
    print("It's a vowel")
else:
    print("Your letter is not a vowel")
        
