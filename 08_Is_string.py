#Python program to get a new string and to check it starts with is or not

_string = input("Enter something: ")
if _string.startswith("Is"):
    print(_string, "\nGood, You're right!")
else:
    print( "Your value has been changed to: Is " + _string )
