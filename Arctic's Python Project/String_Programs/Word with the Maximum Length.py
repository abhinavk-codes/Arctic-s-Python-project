# Program to display the word with the maximum length
sen = input("Enter a sentence: ").lower()

i = 0
w = ""
lwl = 0
lw = ""

while i < len(sen):
    if sen[i] != " ":
        w += sen[i]
    else:
        if len(w) > lwl:
            lwl = len(w)
            lw = w
        w = ""  # reset current word
    i += 1

# Check the last word (after loop ends)
if len(w) > lwl:
    lw = w

print(f"Longest word is: {lw}")
print(f"Length --> {lwl}")
