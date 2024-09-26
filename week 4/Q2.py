def first_last_num(list) :
    if len(list) <=1 :
        return False
    elif  list[0]==list[-1] :
        return True
    else :
         return False

list = list(map(int, input("Enter the numbers to check firts and last element is same or not ").split())) 
print(first_last_num(list))
    