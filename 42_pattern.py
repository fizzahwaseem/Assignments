# j = 1
# for i in range(1,6):
#     print(1, end="")
#     for j in range(2,6):
#         print(2)
# zs
for row in range(1, 6):
    for col in range(1, row+1):
        print(col, end ='')
    print("")
for row in range(4, 0, -1):
    for col in range(1, row + 1):
        print(col, end ='')
    print("")