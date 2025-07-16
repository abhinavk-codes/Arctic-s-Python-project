# Program to check whether a number is Armstrong

n = int(input("Enter a number : "))
d = 0
nd = 0
s = 0
ad = 0
num = n
while num != 0 :
    d = num % 10
    nd += 1
    num //= 10
d = 0
num = n
while num != 0 :
    d = num % 10
    ad = pow(d , nd)
    s += ad
    num //= 10
if s == n :
    print(n, "is an Armstrong Number!")
else :
    print(n, "isn't an Armstrong Number!")

