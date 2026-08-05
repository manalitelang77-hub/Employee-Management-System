class Employee:

    def __init__(self, emp_id, name, age, department, salary, email, phone):

        self.emp_id = emp_id
        self.name = name
        self.age = age
        self.department = department
        self.salary = salary
        self.email = email
        self.phone = phone
        
    def display(self):

        print("Employee ID :", self.emp_id)
        print("Name        :", self.name)
        print("Age         :", self.age)
        print("Department  :", self.department)
        print("Salary      :", self.salary)
        print("Email       :", self.email)
        print("Phone       :", self.phone)