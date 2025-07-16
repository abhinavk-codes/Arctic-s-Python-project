#Program of Character Frequency Counter (Excluding Spaces)
word = str(input("Enter a word : ")).lower()
alpha = "abcdefghijklmnopqrstuvwxyz1234567890"

for letter in alpha:
    count = word.count(letter)
    if count > 0:
        print(f"{letter} → {count}")