num = input("Enter Number : ")
size = len(num)
if(size==4):
    ans = int(num[0:2])**2 + int(num[2:])**2

    print(ans)
else:
    print("Enter 4-digit number!")