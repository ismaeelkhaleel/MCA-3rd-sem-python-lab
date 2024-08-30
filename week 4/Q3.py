def square_list(list) :
    return [i ** 2 for i in list]

numbers = [1,2,3,4,5,6]
squared_numbers  = square_list(numbers)
print(squared_numbers)