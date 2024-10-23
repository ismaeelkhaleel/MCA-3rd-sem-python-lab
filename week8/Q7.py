def create_lists(input_list):
    sorted_list = sorted(input_list)
    mid = len(sorted_list) // 2
    list1 = sorted_list[:mid]  
    list2 = sorted_list[mid:]  
    
    return list1, list2


user_input = input("Enter even number of distinct integers separated by spaces: ").split()

user_list = list(map(int, user_input))

if len(user_list) % 2 != 0:
    print("The list must have an even number of elements.")
else:
    list1, list2 = create_lists(user_list)
    
    print("First list ", list1)
    print("Second list ", list2)
