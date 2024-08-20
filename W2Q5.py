def sum_of_digits(n):
    """Calculate the sum of the digits of a given integer."""
    # Handle negative numbers by taking the absolute value
    n = abs(n)
    
    total_sum = 0
    while n > 0:
        # Add the last digit to the total sum
        total_sum += n % 10
        # Remove the last digit
        n //= 10
    
    return total_sum

# Example usage
if __name__ == "__main__":
    # Input integer
    num = int(input("Enter an integer: "))
    
    # Calculate the sum of the digits
    result = sum_of_digits(num)
    
    # Print the result
    print(f"The sum of the digits of {num} is: {result}")
