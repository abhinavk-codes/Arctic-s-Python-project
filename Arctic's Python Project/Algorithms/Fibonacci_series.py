# Program to display Fibonacci Series!
# Series - 0 1 2 3 5 8 13 21
a: int = 0
b: int = 1
c: int  = 0
n = int(input("Enter the number of terms : "))
i = 1
print("Fibonacci Series till", n , "is" )
while i <= n:
    print(c , end=" ")
    c = a + b
    a = b
    b = c
    i += 1

