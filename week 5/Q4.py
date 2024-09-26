def create_filter_list(list1, list2):
    odd_num_from_list1 = [num for num in list1 if num%2!=0]
    even_num_from_list2 = [num for num in list2 if num%2==0]
    
    result_list = odd_num_from_list1 + even_num_from_list2
    result_list.sort()
    return result_list

list1 = list(map(int,input("Enter the elements of the first list separated by spaces. ").split()))
list2 = list(map(int,input("Enter the elements of the second list separated by spaces. ").split()))

filtered_list = create_filter_list(list1, list2)
print("Your combined list is given below ")
print(filtered_list)