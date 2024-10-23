s = input("Enter a string: ")

vowel = {"a":0,"e":0,"i":0,"o":0,"u":0}

for c in s.lower():
    if c in vowel:
       vowel[c] += 1
maxv=0
maxk=None
for k,v in vowel.items():
    if v>maxv:
        maxv=v
        maxk=k

print("Max vowel in string is ",maxk," -- instances = ",maxv)
