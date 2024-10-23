s = input("Enter string: ")

alph = []
dig = []

for c in s:
    if c.isdigit():
        dig.append(c)
    if c.isalpha():
        alph.append(c)

print(alph)
print(dig)
