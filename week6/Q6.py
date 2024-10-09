def analyze_string(input_string):
    uppercase_count = 0
    lowercase_count = 0
    total_alphabets = 0
    digit_count = 0

    for char in input_string:
        if char.isupper():
            uppercase_count += 1
            total_alphabets += 1
        elif char.islower():
            lowercase_count += 1
            total_alphabets += 1
        elif char.isdigit():
            digit_count += 1

    print(f"Number of uppercase characters: {uppercase_count}")
    print(f"Number of lowercase characters: {lowercase_count}")
    print(f"Total number of alphabets: {total_alphabets}")
    print(f"Number of digits: {digit_count}")

# Accepting input from the user
user_input = input("Enter a string: ")
analyze_string(user_input)
