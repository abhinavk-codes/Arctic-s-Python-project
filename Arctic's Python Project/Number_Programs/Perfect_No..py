# Program to check if a number is Perfect Number
n = int(input("Enter a number : "))
i = 1
s = 0
while i < n:
    if n % i == 0:
        s += i
    i += 1
if s==n :
    print(n, "is a Perfect No.")
else :
    print(n, "isn't a Perfect No.")