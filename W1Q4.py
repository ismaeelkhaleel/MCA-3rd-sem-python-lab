def is_palindrome(number):
    # Convert the number to a string to easily check for palindrome
    num_str = str(number)
    
    # Check if the string is equal to its reverse
    return num_str == num_str[::-1]

def main():
    # Get user input
    try:
        number = int(input("Enter a number to check if it is a palindrome: "))
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
        return
    
    # Check if the number is a palindrome and print the result
    if is_palindrome(number):
        print(f"{number} is a palindrome.")
    else:
        print(f"{number} is not a palindrome.")

if __name__ == "__main__":
    main()
