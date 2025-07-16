# Program to display no. of vowels in a sentence!
st = str(input("Enter a sentence : "))
st1 = st.lower()
nv = 0
l = len(st1)
i = 0
while i < l :
    if st1[i] == 'a' or st1[i] == 'e' or st1[i] == 'i' or st1[i] == 'o' :
        nv += 1
    else :
        nv += 0
    i += 1
print ( "No. of vowels : ", nv)
