#open both files 
file1 = open("C:\\Users\\Admin\\Documents\\ism\\week7\\Department.txt","r")
file2 = open("C:\\Users\\Admin\\Documents\\ism\\week7\\Employee.txt","r")
dept_emp = {}

for dept in file1:
    deptID = dept.split()
    dept_emp[deptID[0]]=[]

for emp_sal in file2:
    emp = emp_sal.split()  
    dept_emp[emp[3]].append(int(emp[2])) 

file1.close()
file2.close()

for dept_id, salaries in dept_emp.items():
    if len(salaries)>0:  
        avg_salary = sum(salaries) / len(salaries)
        print("Department ID: ", dept_id , "-- Average Salary: ",round(avg_salary,2))
    else:
        print("Department ID: ",dept_id, "-- No employees.")
