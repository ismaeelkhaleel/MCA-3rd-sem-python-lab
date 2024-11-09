def add_hra_to_file(input_file_path, output_file_path):
    with open(input_file_path, 'r') as infile, open(output_file_path, 'w') as outfile:
        
        for line in infile:
            name, emp_id, salary, dname = line.strip().split(',')
            salary = float(salary)
            hra = salary * 0.18
            outfile.write(f"{name},{emp_id},{salary},{dname},{hra:.2f}\n")

input_file_path = 'C://Users//CSD//Documents//23CAMSA159//week 8//q7_input.txt'  
output_file_path = 'C://Users//CSD//Documents//23CAMSA159//week 8//q7_output.txt'  
add_hra_to_file(input_file_path, output_file_path)
print("Done!")