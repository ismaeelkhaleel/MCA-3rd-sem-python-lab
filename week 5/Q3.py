import random
import string

digits = string.digits
capitals = string.ascii_uppercase
specials = string.punctuation

password = ""

for i in range(2):
    password += random.choice(capitals)
password += random.choice(digits)
password += random.choice(specials)

for i in range(6):
    password += random.choice(string.printable)

ls = []
ls[:0] = password
random.shuffle(ls)

finalPassword = ''.join(ls)
print(f"your password is : {finalPassword}")
