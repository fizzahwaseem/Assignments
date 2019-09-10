#Python program which accepts the user's first and last name and print them in reverse order with a space between them
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
# f, l = first_name, last_name
# print(l, f)
full = first_name + " " + last_name
full = full[::-1]
print(full)