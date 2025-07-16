# Program to calculate sum of digits of a number!
n = int(input("Enter a number : "))
num = n
d = 0
s = 0
while num != 0 :
    d = num % 10
    s += d
    num //= 10
print("Sum of digits of ", n , "is" , s)
