def count_digits(n):
    # Handle the case where n is negative
    n = abs(n)
    
    # Special case for zero
    if n == 0:
        return 1
    
    count = 0
    while n > 0:
        # Remove the last digit
        n //= 10
        # Increment the digit count
        count += 1
        
    return count

# Example usage
if __name__ == "__main__":
    # Input integer
    num = int(input("Enter an integer: "))
    
    # Count the number of digits
    result = count_digits(num)
    
    # Print the result
    print("Total number of digits:", result)
