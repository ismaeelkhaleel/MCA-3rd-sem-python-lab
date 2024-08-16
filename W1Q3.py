def get_numbers_from_user():
    numbers = []
    print("Please enter 20 numbers:")
    while len(numbers) < 20:
        try:
            number = int(input(f"Enter number {len(numbers) + 1}: "))
            numbers.append(number)
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
    return numbers

def print_numbers_divisible_by_5(numbers):
    print("Numbers divisible by 5:")
    for number in numbers:
        if number % 5 == 0:
            print(number)

def main():
    numbers = get_numbers_from_user()
    print_numbers_divisible_by_5(numbers)

if __name__ == "__main__":
    main()
