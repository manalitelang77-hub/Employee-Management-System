from employee import Employee
from file_handler import save_all_employees,load_employees
from employee_manager import add_employee,view_employee,search_employee,update_employee,delete_employee,sort_employees,dashboard,export_to_csv  
from menu import display_menu


employees = load_employees()


while True:

    display_menu() 
    choice = input("Enter your choice: ")

    # ---------------- ADD EMPLOYEE ---------------- #
    if choice == "1":
        add_employee(employees)
# ---------------- VIEW EMPLOYEES ---------------- #

    elif choice == "2":
        view_employee(employees)

    # ---------------- SEARCH EMPLOYEE ---------------- #

    elif choice == "3":
         search_employee(employees)

    # ---------------- UPDATE EMPLOYEE ---------------- #

    elif choice == "4":
       update_employee(employees) 
        
        #---------------- DELETE EMPLOYEE ---------------- # 
    elif choice == "5": 
     delete_employee(employees)
     
    elif choice == "6": 
        sort_employees(employees) 
        
    elif choice == "7": 
        dashboard(employees) 
            
            #---------------- EXIT ---------------- # 
    elif choice == "8":
        export_to_csv(employees)
        
    elif choice == "9":
        print("\nThank You for using Employee Management System.")
        break

    else:
        print("\nInvalid Choice. Please Try Again.")