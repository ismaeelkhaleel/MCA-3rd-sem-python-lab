dict1 = {}

n = int(input("Enter number of key-value pairs of dictionary: "))

for i in range(n):
    key = input("Enter Name: ")
    dict1[key] = input("Enter Ph.No: ")

print(dict1)


key = input("Enter Name: ")
print(dict1.get(key,"Do not exist"))


