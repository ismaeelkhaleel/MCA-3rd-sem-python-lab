import random

user_string = input("Enter the string : ")

if user_string:
    
    random_character = random.choice(user_string)
    print(f"The random character is {random_character}")
else:
    print("The string can not be empty")