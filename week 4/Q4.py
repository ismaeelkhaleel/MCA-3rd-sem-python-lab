def iterate_list(list1, list2) :
    for item1, item2 in zip(list1, reversed(list2)) :
        print(f"List 1 : {item1}, List 2 : {item2}")
        
list1 = [1,2,3,4,5]
list2 = ['a', 'b', 'c', 'd', 'e']
iterate_list(list1, list2)