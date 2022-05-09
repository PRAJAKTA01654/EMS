lstEmployees = []
deptlist = []

###### Employee Class
class Employee:
    num_of_emps = 0
    emp_id_num = 0
    emp_id = None

    def __init__(self, first, last, start_date, salary, dept):
        self.first = first
        self.last = last
        self.start_date = start_date
        self.salary = salary
        self.dept = dept

        Employee.num_of_emps += 1
        Employee.emp_id_num += 1
        Employee.emp_id = 'EMP' + str(Employee.emp_id_num)

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

######## Department Class
class Department:
    num_of_depts = 0
    dept_dict = {}
    # dict_emp_list = []

    def __init__(self, dept_name, dept_budget, dept_phone, emp_list=None):
        self.dept_name = dept_name
        self.dept_budget = dept_budget
        self.dept_phone = dept_phone
        if emp_list is None:
            self.emp_list = []
        else:
            self.emp_list = emp_list

        Department.num_of_depts += 1
        Department.dept_dict[dept_name] = {"dept_budget": dept_budget, "dept_phone": dept_phone, "Employee_list": emp_list}


    def add_emp(self, emp):
        if emp not in self.emp_list:
            self.emp_list.append(emp)

    def remove_emp(self, emp):
        if emp in self.emp_list:
            self.emp_list.remove(emp)

    def show_emps(self):
        for emp in self.emp_list:
            print('==>', emp)

    def export_dept(self):
        with open("file.txt", "w") as output:
            output.write(str(Department.dept_dict))
        print('Dept :===>>>> {}'.format(Department.dept_dict))

#### Custom Exception class
class CustomException(Exception):
    pass

def search_dept(dept_name):
    for dept in deptlist:
        if dept_name == dept[0]:
            print("------->  Details of the department {} is :".format(dept[0]))
            print("Department Name: {}".format(dept[1].dept_name))
            print("Department budget: {} ".format(dept[1].dept_budget))
            print("Department Phone Number: {}".format(dept[1].dept_phone))
            print("Department Employee List : {}".format(dept[1].emp_list))
            return dept
    return -1

def add_employee():
    first = input("Enter first name of employee : ")
    last = input("Enter last name of employee : ")
    salary = input("Enter employee Salary: ")
    start_dt = input("Enter employee Start date: ")
    dept = input("Enter employee department: ")
    srch_dept = search_dept(dept)
    while srch_dept == -1:
        print("The entered department name is not valid. Valid Departments are listed below: ")
        for dept in deptlist:
            print("------->  {}".format(dept[0]))
        dept = input("Please enter a valid name: ")
        srch_dept = search_dept(dept)

    emp_details = Employee(first, last,  start_dt, salary, dept )
    lstEmployees.append([Employee.emp_id, emp_details])
    srch_dept[1].add_emp(emp_details.fullname())

def print_employee():
    for employee in lstEmployees:
        print("-------> Details of employee with Employee ID : {} {}".format(employee[0], "---------------"))
        print("Employee Name: {}".format(employee[1].fullname()))
        print("Employee Salary: {} ".format(employee[1].salary))
        print("Employee Start Date: {}".format(employee[1].start_date))
        print("Employee Department: {}".format(employee[1].dept))


def search_emp():
    emp_id = input("Enter employee Employee Id: ")
    for employee in lstEmployees:
        if emp_id == employee[0]:
            print("------->  Employee with Employee ID : {} is found {}".format(employee[0], "---------------"))
            print("Employee Name: {}".format(employee[1].fullname()))
            print("Employee Salary: {} ".format(employee[1].salary))
            print("Employee Start Date: {}".format(employee[1].start_date))
            print("Employee Department: {}".format(employee[1].dept))
            return employee
    return -1

def edit_employee():
    search = search_emp()
    if search == -1:
        print("Employee not found...")
    else:
        first = input("Enter first name of employee : ")
        last = input("Enter last name of employee : ")
        salary = input("Enter employee Salary: ")
        start_dt = input("Enter employee Start date: ")
        dept = input("Enter employee department: ")

        if search[1].dept != dept:
            print("Removing the employee from oild department : {}".format(search[1].dept))
            srch_dept = search_dept(search[1].dept)
            if srch_dept == -1:
                print("Old Department nont found : {}".format(search[1].dept))
            else:
                srch_dept[1].remove_emp(search[1].fullname())
                print("Successfully removed the employee name from oild department : {} --> {}".format(search[1].dept, search[1].fullname()))

        srch_dept = search_dept(dept)
        while srch_dept == -1:
            print("The entered department name is not valid. Valid Departments are listed below: ")
            for dept in deptlist:
                print("------->  {}".format(dept[0]))
            dept = input("Please enter a valid name: ")
            srch_dept = search_dept(dept)

        search[1].first = first
        search[1].last = last
        search[1].start_date = start_dt
        search[1].salary = salary
        search[1].dept = dept
        srch_dept[1].add_emp(search[1].fullname())

def add_dept():
    dept_name = input("Enter Department Name : ")
    dept_budget = input("Enter Department Budget : ")
    dept_phone = input("Enterdepartment phone number: ")

    dept = Department(dept_name, dept_budget,  dept_phone, None )
    deptlist.append([dept.dept_name, dept])

def view_depts():
    for dept in deptlist:
        print("------->  Details of the department {} is :".format(dept[0]))
        print("Department Name: {}".format(dept[1].dept_name))
        print("Department budget: {} ".format(dept[1].dept_budget))
        print("Department Phone Number: {}".format(dept[1].dept_phone))
        print("Department Employee List : {}".format(dept[1].emp_list))

def edit_dept():
    find_dept = input("Enter Department name to edit: ")
    search = search_dept(find_dept)
    if search == -1:
        print("Department not found...")
    else:
        dept_name = input("Enter Department Name : ")
        dept_budget = input("Enter Department Budget : ")
        dept_phone = input("Enterdepartment phone number: ")
        search[1].dept_name = dept_name
        search[1].dept_budget = dept_budget
        search[1].dept_phone = dept_phone

def remove_dept():
    find_dept = input("Enter Department name to remove from system: ")
    search = search_dept(find_dept)
    if search == -1:
        print("Department not found...")
    else:
        deptlist.remove(search)

def view_dept_emp():
    find_dept = input("Enter Department name to view details: ")
    search = search_dept(find_dept)
    if search == -1:
        print("Department not found...")
    else:
        print("Below are the employees under Department {}".format(search[0]))
        search[1].show_emps()

def export_dept_det():
    deptlist[0][1].export_dept()

def main():
    while True:
        print('----------------------------------------------\n')
        print('      Welcome to the Employee Data System    -\n')
        print('----------------------------------------------\n')
        print('[1] Add an Employee: \n')
        print('[2] View All Employees: \n')
        print('[3] Search Employee with Employee Id: \n')
        print('[4] Edit Employees information: \n')
        print('[5] Departments: \n')
        print('[6] Exit the system : \n')
        user_option = input("Please select an option: ")
        if user_option == "1":
            add_employee()
        elif user_option == "2":
            print('\n' * 3)
            print_employee()
            print('\n' * 3)
        elif user_option == "3":
            found = search_emp()
            if found == -1:
                print("Employee not found...")
        elif user_option == "4":
            edit_employee()
        elif user_option == "5":
            print('----------------------------------------------\n')
            print('      Welcome to the Department Page    -\n')
            print('----------------------------------------------\n')
            print('[1] Add a Department: \n')
            print('[2] View All Department: \n')
            print('[3] Search Department information: \n')
            print('[4] Edit Department information: \n')
            print('[5] Remove Departments: \n')
            print('[6] View Employee list in the Department : \n')
            print('[7] Export Employees information : \n')
            user_option = input("Please select an option: ")
            if user_option == "1":
                add_dept()
            elif user_option == "2":
                view_depts()
            elif user_option == "3":
                find_dept = input("Enter Department name to search: ")
                search_dept(find_dept)
            elif user_option == "4":
                edit_dept()
            elif user_option == "5":
                remove_dept()
            elif user_option == "6":
                view_dept_emp()
            elif user_option == "7":
                export_dept_det()
            else:
                print("Please select a valid option for department operation...")
        elif user_option == '6':
            exit()
        else:
            print("Please select a valid option...")

if __name__ == "__main__":
    main()



