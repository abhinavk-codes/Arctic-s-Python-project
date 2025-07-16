# Program to input 5 numbers from user and check whether they're prime using a function!
i = 1
def is_prime(n):
    i = 1
    c = 0
    while i <= n :
        if n % i == 0 :
            c += 1
        i += 1
    if c == 2 :
        return "Prime"
    elif n == 1 :
        return "Neither prime nor composite"
    else :
        return "Composite"

for i in range (5) :
    n = int(input("Enter a number : "))
    if n!=1 :
        print(f"{n} is a {is_prime(n)} No.")
    else :
        print(f"{n} is {is_prime(n)} No.")
