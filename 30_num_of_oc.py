#Python program to count the number occurrence of a specific character in a string
str_ = input("Enter a string :")
char_ = input("Enter a character: ")
char_count = 0
for i in str_:
    if char_ == i:
        char_count += 1
print(char_count)
