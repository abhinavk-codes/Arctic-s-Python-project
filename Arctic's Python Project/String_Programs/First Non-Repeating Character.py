# Program to get a First Non-Repeating Character

# Also considered a classic string algorithm problem
# Could be placed in Algorithms folder as well


st = str(input("Enter a sentence : ")).lower()
for word in st :
    if st.count(word) == 1 :
        print(f"The first non repeating word : {word}")
        break
    else :
        print(f"No non-repeating word!")
        break
