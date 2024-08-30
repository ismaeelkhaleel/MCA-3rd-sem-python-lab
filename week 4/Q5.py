def count_occurrences(tp, item) :
    return tp.count(item)

tp1 = (50, 10, 60, 70, 50)
item_to_count = 50
count = count_occurrences(tp1, item_to_count)
print(f"The item {item_to_count} occurs {count} times in the tuple")