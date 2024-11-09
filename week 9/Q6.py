def count_courses_per_program(file_path):
    program_count = {}

    with open(file_path, 'r') as f:
        next(f)  
        for line in f:
            program, course = line.strip().split(',')
            program_count[program] = program_count.get(program, 0) + 1

    for program, count in program_count.items():
        print(f"{program}-{count:02d}")

file_path = 'C://Users//CSD//Documents//23CAMSA159//week 8//q6.txt'
count_courses_per_program(file_path)