from file_handler import save_all_employees
from employee import Employee

def add_employee(employees):
        
                emp_id = int(input("Enter Employee ID: "))
                for emp in employees:

                   if emp.emp_id == emp_id:
                       print("\n❌ Employee ID already exists.")
                       return
                   
                name = input("Enter Employee Name: ")
                
                while True: 
                 age = int(input("Enter Age: "))
                 if age>=18 and age<=60:
                    break
                 print("proper age entered")
                else:
                    print("❌ Age must be between 18 and 60.")
                
                department = input("Enter Department: ")
                
                while True: 
                 salary = float(input("Enter Salary: "))
                 if salary>0:
                     break
                 print("proper salary entered") 
                else:
                 print("❌ Salary must be greater than 0.") 
                 
                while True: 
                 email = input("Enter Email: ")
                 if "@"in email and "."in email and len(email)>5:
                     break 
                 print("proper email entered") 
                else:
                   print("❌ Invalid Email Address.") 
                
                
                while True: 
                 phone = input("Enter Phone Number: ")
                 if phone.isdigit() and len(phone) == 10:
                     break
                 print("proper phone number entered") 
                else:
                 print("❌ Phone Number must be a 10-digit number.")  
        
                emp = Employee(
                    emp_id,
                    name,
                    age,
                    department,
                    salary,
                    email,
                    phone
                )
        
                employees.append(emp)
                print("\n✅ Employee Added Successfully!")
                save_all_employees(employees )
def view_employee(employees ): 
            
            if len(employees) == 0:
                        print("\nNo Employees Found.")
            
            else:
                        print("\n========== Employee List ==========")
            
            for emp in employees:
                 emp.display()
                 print("-----------------------------------")
       
def search_employee(employees): 
            print("\n========== Search Employee By ==========") 
            print("1. Employee ID")
            print("2. Employee Name")
            choice = int(input("Enter your choice: ")) 
            
            if choice == "1":
                emp_id = int(input("Enter Employee ID: "))
                for emp in employees:
                    if emp.emp_id == emp_id:
                        emp.display()
                        return
                    print("Employee Not Found.")
            elif choice == "2":
                name = input("Enter Employee Name: ")
                found = False
                for emp in employees:
                    if emp.name.lower() == name.lower():
                        emp.display()
                        print("----------------------")
                        found = True
                        if found == False:
                            print("Employee Not Found.")
            elif choice == "3":
                department = input("Enter Department: ")
                found = False
                for emp in employees:
                 if emp.department.lower() == department.lower():
                     emp.display()
                     print("----------------------------")
                     found = True
                     if found == False:
                      print("No Employee Found.")
            
def update_employee(employees): 
             update_id=int(input("Enter Employee ID to Update: ")) 
             found=False 
             for emp in employees: 
                 if emp.emp_id==update_id: 
                             emp.name=input("Enter Employee Name: ") 
                             emp.age=int(input("Enter Age: ")) 
                             emp.department=input("Enter Department: ") 
                             emp.salary=float(input("Enter Salary: ")) 
                             emp.email=input("Enter Email: ") 
                             emp.phone=input("Enter Phone Number: ") 
                             print("\n✅ Employee Updated Successfully!") 
                             save_all_employees(employees)
                             found=True 
                             break
             
                 if found == False:
                         print("\n❌ Employee Not Found.")
def delete_employee(employees): 
            delete_id=int(input("Enter Employee ID to Delete:  "))
            found=False
            for emp in employees:
               if emp.emp_id==delete_id:
                                employees.remove(emp)
                                print("✅ Employee Deleted Successfully!")
                                save_all_employees(employees )
                                found=True 
                                break 
               if found == False:
                                print("❌ Employee Not Found")
                                
def sort_employees(employees):

    print("\nSort By")
    print("1. Salary (Low to High)")
    print("2. Salary (High to Low)")
    print("3. Name (A-Z)")
    print("4. Name (Z-A)")

    choice = input("Enter your choice: ")

    if choice == "1":
        employees.sort(key=lambda emp: emp.salary)

    elif choice == "2":
        employees.sort(key=lambda emp: emp.salary, reverse=True)

    elif choice == "3":
        employees.sort(key=lambda emp: emp.name.lower())

    elif choice == "4":
        employees.sort(key=lambda emp: emp.name.lower(), reverse=True)

    else:
        print("❌ Invalid Choice")
        return

    print("\nEmployees Sorted Successfully!\n")

    for emp in employees:
        emp.display()
        print("---------------------------")
        
def dashboard(employees):

    if len(employees) == 0:
        print("No Employees Found.")
        return

    print("\n========== Employee Dashboard ==========")

    total = len(employees)

    highest = employees[0].salary
    lowest = employees[0].salary

    total_salary = 0

    for emp in employees:

        total_salary += emp.salary

        if emp.salary > highest:
            highest = emp.salary

        if emp.salary < lowest:
            lowest = emp.salary

    average = total_salary / total

    print("Total Employees :", total)
    print("Highest Salary  :", highest)
    print("Lowest Salary   :", lowest)
    print("Average Salary  :", average)

    print("========================================")
def export_to_csv(employees):

    file = open("employees.csv", "w")

    file.write("Employee ID,Name,Age,Department,Salary,Email,Phone\n")

    for emp in employees:

        file.write(
            f"{emp.emp_id},{emp.name},{emp.age},{emp.department},{emp.salary},{emp.email},{emp.phone}\n"
        )

    file.close()

    print("Employees exported successfully!")
    