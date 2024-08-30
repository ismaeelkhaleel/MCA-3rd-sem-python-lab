def first_last_num(list) :
    if len(list) <=1 :
        return False
    elif  list[0]==list[-1] :
        return True
    else :
         return False
     
print(first_last_num([1,2,3,4,1]))
    