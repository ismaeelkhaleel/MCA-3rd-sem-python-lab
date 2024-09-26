import numpy as np

rows = int(input("Enter the number of rows : "))
cols = int(input("Enter the number of cols : "))
# Create a numpy array

array = np.random.randint(0,100, size=(rows, cols))
print("\nOriginal array is : \n")
print(array)
  

# Case 1: Sort the array by the second row
sorted_by_second_row = array[:,array[1,:].argsort()]
print("\nArray sorted by the second row:")
print(sorted_by_second_row)

# Case 2: Sort the array by the second column
sorted_by_second_column = array[array[:,1].argsort(),:]
print("\nArray sorted by the second column:")
print(sorted_by_second_column)
