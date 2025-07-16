#Program to Reverse Words in a Sentence!
# sen = str (input("Enter a sentence : ")).strip()
# words = sen.split()
# i = len(words) - 1
# while i >= 0 :
#     print(words[i] , end = " ")
#     i -= 1

#Fine-tuned program to do the same!
# Ask the user to enter a sentence and remove unwanted spaces at start/end
sentence = input("Enter a sentence: ").strip()

# Step-by-step explanation of the next line:
# 1. sentence.split() → breaks the sentence into a list of words
#    e.g., "I love Python" becomes ['I', 'love', 'Python']
# 2. [::-1] → reverses the list of words
#    So ['I', 'love', 'Python'] becomes ['Python', 'love', 'I']
# 3. " ".join(...) → joins the reversed list into a new string using space as separator
#    So ['Python', 'love', 'I'] becomes "Python love I"

reversed_sentence = " ".join(sentence.split()[::-1])

# Print the final reversed sentence
print("Reversed sentence:", reversed_sentence)
