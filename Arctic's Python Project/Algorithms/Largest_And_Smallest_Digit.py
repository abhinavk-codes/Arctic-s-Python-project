# Program to find and display the largest and smallest digit of the number!
n = int(input("Enter a number : "))
num = n
d = 0
l = 0
s = 9
while num > 0 :
    d = num % 10
    if d > l :
        l = d
    elif d < s :
        s = d
    num //= 10
print (f"The Largest digit of {n} is {l}")
print(f"The smallest digit of {n} is {s}")