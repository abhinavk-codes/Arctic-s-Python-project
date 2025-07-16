# Program to input a number from user and check whether its prime using a function!
n = int(input("Enter a number: "))

def is_prime(n):
    i = 1
    c = 0
    while i <= n :
        if n % i == 0 :
            c += 1
        i += 1
    if c == 2 :
        return "Prime"
    else :
        return "Composite"
print(f"{n} is a {is_prime(n)} No.")