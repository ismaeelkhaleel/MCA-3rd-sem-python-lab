def factorial(n):
    """Calculate the factorial of a given number using a loop."""
    if n < 0:
        return "Factorial is not defined for negative numbers."
    elif n == 0:
        return 1  # The factorial of 0 is 1
    else:
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result

# Example usage
if __name__ == "__main__":
    # Input number
    num = int(input("Enter a number to find its factorial: "))
    
    # Calculate the factorial
    result = factorial(num)
    
    # Print the result
    print(f"The factorial of {num} is: {result}")
