from employee import Employee 

def save_all_employees(employees ):
    file = open("employees.txt", "w")
    for emp in employees:
        file.write(str(emp.emp_id) + "\n")
        file.write(emp.name + "\n")
        file.write(str(emp.age) + "\n")
        file.write(emp.department + "\n")
        file.write(str(emp.salary) + "\n")
        file.write(emp.email + "\n")
        file.write(emp.phone + "\n")
    file.close()

def load_employees():
    employees=[]
    try:
        file=open("employees.txt", "r") 
        lines = file.readlines()
        file.close()

        for i in range(0, len(lines), 7):
         emp_id = int(lines[i].strip())
         name = lines[i + 1].strip()
         age = int(lines[i + 2].strip())
         department = lines[i + 3].strip()
         salary = float(lines[i + 4].strip())
         email = lines[i + 5].strip()
         phone = lines[i + 6].strip()

         emp = Employee( emp_id,name, age,department,salary,email,phone)
         employees.append(emp)
    except FileNotFoundError: 
        pass
    return employees 
