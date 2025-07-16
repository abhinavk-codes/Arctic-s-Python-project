# Program to input 5 five names in list and then display the longest name!
names = []

# Input 5 names
for i in range(5):
    name = input(f"Enter name {i + 1}: ")
    names.append(name)

# Find the logest name using max() with key=len
longest = max(names, key=len)

print(f"The longest name is: {longest}")
