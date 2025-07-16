# Program to display frequency of each digit in a number!
n = int(input("Enter a number: "))
freq = [0] * 10  # Creates a list with 10 zeros for digits 0 to 9

while n != 0:
    digit = n % 10        # Get the last digit
    freq[digit] += 1      # Increase the count at that digit’s position
    n //= 10              # Remove the last digit

for i in range(10):
    print(f"{i} occurs {freq[i]} times")
