# Program to display even no. from a list of no. and list must have user input no.s
nums = []
even = []
for i in range(5) :
    val = int(input(f"Enter a number at {i} th index : "))
    nums.append(val)
for num in nums :
    if num % 2 == 0 :

     even.append(num)
print(f"Even no(s) is/are : {even}")
