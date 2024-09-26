import numpy as np

rows = int(input("Enter the number of rows : "))
cols = int(input("Enter the number of cols : "))
# Create a numpy array

array = np.random.randint(0,100, size=(rows, cols))
print("\nOriginal array is : \n")
print(array)
  
# Get odd rows and even columns
result = array[::2, 1::2]
print("\nArray of odd rows and even columns from the original array : \n")
print(result)