# Program to print Right Half Pyramid Pattern
#     *
#    **
#   ***
#  ****
# *****

n = int(input("Enter number of rows : "))
# i = 1
# print("The pattern is : ")
# while i <=n :
#     j = 1
#     while j <=(n-i) :
#         print(f" ",end=" ")
#         j += 1
#     k = 1
#     while k<=i :
#         print(f"*",end=" ")
#         k += 1
#     print()
#     i += 1


for i in range(1, n + 1):
    print(" " * (n - i) + "*" * i)
