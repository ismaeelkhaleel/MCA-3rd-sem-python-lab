numbers = []
for i in  range(20):
    num = int(input("Enter the number"))
    numbers.append(num)

print("The numbers are given below which are divisible by 5")
for num in numbers:
    if num%5==0:
        print(num)