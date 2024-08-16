def calculate_cubes(up_to):
    return {number: number ** 3 for number in range(1, up_to + 1)}

def main():
    try:
        up_to = int(input("Enter the upper limit to calculate cubes from 1 to that number: "))
        if up_to < 1:
            print("Please enter a number greater than 0.")
            return
        cubes = calculate_cubes(up_to)
        print("Cubes of numbers from 1 to", up_to, ":")
        for number, cube in cubes.items():
            print(f"{number}^3 = {cube}")
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

if __name__ == "__main__":
    main()