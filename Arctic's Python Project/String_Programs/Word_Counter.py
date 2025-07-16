# Take input and convert to lowercase to avoid case mismatch
sentence = input("Enter a sentence: ").lower()

# Split the sentence into a list of words
words = sentence.split()

# Create an empty dictionary to store word counts
freq = {}

# Loop through each word and count using .get()
for word in words:
    freq[word] = freq.get(word, 0) + 1

# Print the word frequencies
print("\nWord Frequency:")
for word, count in freq.items():
    print(word, "→", count)
