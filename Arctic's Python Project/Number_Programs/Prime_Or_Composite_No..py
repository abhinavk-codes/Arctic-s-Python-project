# Program to check to whether a number is prime or composite
n = int(input("Enter a number : "))
i = 1
c = 0
while i<=n:
    if n % i == 0:
        c += 1
        i += 1
    else :
        i += 1
if c == 2 :
   print( n, "is a Prime No. ")
else :
   print( n, "isn't a Prime No.")
