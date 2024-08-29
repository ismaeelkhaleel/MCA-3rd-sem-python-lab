num = int(input("Enter a integer"))
count = 0
while num>0: 
    count+=1
    num = num//10
    
print(count)

# num = int(input("Enter a integer"))
# count = 0
# sum = 0
# rev = 0
# while num > 0:
#     rem = num%10
#     rev = rev*10+rem
#     num //=10
# while rev>0: 
#     digit = rev%10
#     count+=1
#     if count%2!=0:
#         sum+=digit
#     rev = rev//10
    
# print(sum)