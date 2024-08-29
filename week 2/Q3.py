num1 = int(input("Enter the lower limit"))
num2 = int(input("Enter the upper limit"))

for i in range(num1, num2) :
    for j in range(i) :
        if(i%j!=0) :
            break
        else :
            print(i)