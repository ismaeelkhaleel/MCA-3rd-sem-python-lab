import re
from collections import Counter
import string

def replace_max_word_with_aligarh(input_file_path, output_file_path):
        with open(input_file_path, 'r') as infile:
            text = infile.read()
        
        translator = str.maketrans('', '', string.punctuation)
        normalized_text = text.lower().translate(translator)
        
        words = normalized_text.split()
        word_counts = Counter(words)

        if word_counts:
            max_word, max_count = word_counts.most_common(1)[0]
        else:
            print("No words found in the input file.")
            return
        
        pattern = r'\b' + re.escape(max_word) + r'\b'
        
        updated_text = re.sub(pattern, "Aligarh", text, flags=re.IGNORECASE)
        
        with open(output_file_path, 'w') as outfile:
            outfile.write(updated_text)
        
        print("Replacement completed successfully.")

input_file_path = 'C://Users//CSD//Documents//23CAMSA159//week 10//input.txt'  
output_file_path = 'C://Users//CSD//Documents//23CAMSA159//week 10//output.txt'

# Call the function
replace_max_word_with_aligarh(input_file_path, output_file_path)