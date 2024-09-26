def square_list(list) :
    return [i ** 2 for i in list]

numbers = list(map(int, input("Enter the numbers to squared them, separate by space ").split()))
squared_numbers  = square_list(numbers)
print(squared_numbers)