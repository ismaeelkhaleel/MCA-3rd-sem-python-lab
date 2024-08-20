def extract_digits_reverse(n):
    # Handle negative numbers by making them positive
    n = abs(n)
    
    # Convert the number to a string
    num_str = str(n)
    
    # Create an empty list to store the digits
    digits = []
    
    # Iterate through the string in reverse order and append each digit to the list
    for digit in reversed(num_str):
        digits.append(digit)
    
    return digits

# Example usage
if __name__ == "__main__":
    # Input integer
    num = int(input("Enter an integer: "))
    
    # Extract digits in reverse order
    result = extract_digits_reverse(num)
    
    # Print the result
    print("Digits in reverse order:", result)
