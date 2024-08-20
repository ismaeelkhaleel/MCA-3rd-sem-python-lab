def is_prime(num):
    """Check if a number is prime."""
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def display_primes(start, end):
    """Display all prime numbers in the given range [start, end]."""
    if start > end:
        print("Invalid range: start should be less than or equal to end.")
        return
    
    print(f"Prime numbers between {start} and {end}:")
    for num in range(start, end + 1):
        if is_prime(num):
            print(num, end=' ')
    print()  # for newline

# Example usage
if __name__ == "__main__":
    # Input range
    start = int(input("Enter the start of the range: "))
    end = int(input("Enter the end of the range: "))
    
    # Display prime numbers in the range
    display_primes(start, end)
