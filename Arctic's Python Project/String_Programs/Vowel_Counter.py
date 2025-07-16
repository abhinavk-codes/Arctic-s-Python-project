# Program to count the frequency of vowels in a sentence!

# st = str(input("Enter a sentence : "))
# st1 = st.lower()
# print(f"a occurs {st1.count('a')} times")
# print(f"e occurs {st1.count('e')} times")
# print(f"i occurs {st1.count('i')} times")
# print(f"o occurs {st1.count('o')} times")
# print(f"u occurs {st1.count('u')} times")

# Better adn efficient version of the code by ChatGPT --

st = input("Enter a sentence: ").lower()
vowels = "aeiou"

for v in vowels:
    print(f"{v} occurs {st.count(v)} times")

