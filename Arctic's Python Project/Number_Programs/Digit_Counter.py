# Program to count and display the no. of digits a number
n  = int(input("Enter a number : "))
num = n
d = 0
nd = 0
while num > 0:
    d = num % 10
    nd += 1
    num //= 10
print ( "No. of digits of" , n , "is" , nd)    