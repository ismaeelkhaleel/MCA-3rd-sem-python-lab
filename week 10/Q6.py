def merge_employee_department(emp_file_path, dept_file_path, output_file_path):
    
    departments = {}
    with open(dept_file_path, 'r') as dept_file:
        for line in dept_file:
            did, dname, dlocation = line.strip().split(',')
            departments[did] = (dname, dlocation)

    with open(output_file_path, 'w') as output_file:
    
        with open(emp_file_path, 'r') as emp_file:
            for line in emp_file:
                name, eid, salary, did = line.strip().split(',')
                if did in departments:
                    dname, dlocation = departments[did]
                    
                    output_file.write(f"{name},{eid},{salary},{did},{dname},{dlocation}\n")

# File paths
emp_file_path = 'C://Users//CSD//Documents//23CAMSA159//week 10//employees.txt'
dept_file_path = 'C://Users//CSD//Documents//23CAMSA159//week 10//departments.txt'
output_file_path = 'C://Users//CSD//Documents//23CAMSA159//week 10//merged_output.txt'

# Call the merge function
merge_employee_department(emp_file_path, dept_file_path, output_file_path)