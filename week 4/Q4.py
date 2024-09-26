def iterate_list(list1, list2) :
    for item1, item2 in zip(list1, reversed(list2)) :
        print(f"{item1}, {item2}")
        
list1 = list(map(int, input("Enter the elements of the first list, separate by space ").split()))
list2 = list(map(int, input("Enter the elements of the first list, separate by space ").split()))
iterate_list(list1, list2)