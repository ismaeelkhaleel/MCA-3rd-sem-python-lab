def find_max_alphabet_instances(file_path):
    from collections import Counter
 
    alphabet_count = Counter()

    with open(file_path, 'r') as f:
        for line in f:    
            alphabet_count.update(char.lower() for char in line if char.isalpha())
        
         
    if not alphabet_count:
        print("No alphabet characters found in the file.")
        return

         
    max_count = max(alphabet_count.values())
        
         
    max_alphabets = [char for char, count in alphabet_count.items() if count == max_count]

    print(f"Alphabets with the maximum occurrences ({max_count} instances): {', '.join(max_alphabets)}")


file_path = 'C://Users//CSD//Documents//23CAMSA159//week 8//q5.txt'
find_max_alphabet_instances(file_path)