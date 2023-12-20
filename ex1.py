class Employee:
    """Common base class for all employees"""
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        self.tasks = {}
        Employee.empCount += 1

    def display_emp_count(self):
        "Displays the number of employees"
        print(f"Total number of employee(s) is {Employee.emp_count}")

    def display_employee(self):
        print("Name : ", self.name, ", Salary: ", self.salary)

    def __del__ (self):
        Employee.empCount -=1


    def update_salary(self, new_salary):
        self.salary = new_salary

##    def add_task(self, task_name):
##        self.tasks[task_name] = "New"   # needs tasks defined before (in __init__)
##
##    def update_tasks(self, task_name, status):
##        self.tasks[task_name] = status
    def modify_task(self, task_name, status="New"):
        self.tasks[task_name]=status

    def display_task(self, status):
        print(f"Taskuri cu statusul {status}")
        for name in self.tasks.keys():
            if self.tasks[name] == status:
                print(name)

class Manager (Employee):
    mgr_count = 0
    department = "E10"
    def __init__(self, name, salary, department):
        self.name = name
        self.salary = salary
        self.department = department
        self.mgr_count += 1

    def display_employee(self):
        print("Department: ", self.department)
        
manager1 = Manager("Alex", 5000, "Marketing")
manager2 = Manager("Dia", 5000, "Marketing")
manager3 = Manager("Gabi", 5000, "Marketing")
manager4 = Manager("Mario", 5000, "Marketing")
manager5 = Manager("David", 5000, "Marketing")
manager1.display_employee()
manager2.display_employee()
manager3.display_employee()
manager4.display_employee()
manager5.display_employee()
employ1 = Employee("Nustiu",4000)
print(employ1.empCount)
