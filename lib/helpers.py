from models.department import Department
from models.employee import Employee


def exit_program():
    print("Goodbye!")
    exit()

# We'll implement the department functions in this lesson


def list_departments():
    departments = Department.get_all()
    for department in departments:
        print(department)


def find_department_by_name():
    name = input("Enter the department's name: ")
    department = Department.find_by_name(name)
    if department:
        print(department)
    else:
        print(f'Department {name} not found')


def find_department_by_id():
    dep_id = input("Enter the department's id: ")
    department = Department.find_by_id(dep_id)
    if department:
        print(department)
    else:
        print(f"Department {dep_id} not found")


def create_department():
    name = input("Enter the department's name: ")
    location = input("Enter the department's location: ")
    try:
        department = Department.create(name, location)
        print(f"success: {department}")
    except Exception as e:
        print(f"Error creating department: {e}")



def update_department():
    department_id = input("Enter the department's id: ")
    department = Department.find_by_id(department_id)
    if department:
        try:
            department_name = input("Enter the department's name: ")
            department_location = input("Enter the department's location: ")

            department.name = department_name
            department.location = department_location

            department.update()
            print(f"success: {department}")
        except Exception as err:
            print(f"Error updating the department, {err}")
    else:
        print(f"Did not find department with id: {department_id}")



def delete_department():
    department_id = input("Enter the department id: ")
    department = Department.find_by_id(department_id)

    if department:
        department.delete()
        print(f'Department {department_id} deleted')
    else:
        print(f"Department {department_id} deleted")


# You'll implement the employee functions in the lab

def list_employees():
    employees = Employee.get_all()
    for employee in employees:
        print(employee)


def find_employee_by_name():
    employee_name = input("Enter employee name: ")
    employee = Employee.find_by_name(employee_name) 
    if employee:
        print(employee)
    else:
        print(f"{employee_name} not found")
    


def find_employee_by_id():
    employee_id = input("Enter the employee's id: ")
    employee = Employee.find_by_id(employee_id)
    if employee:
        print(employee)
    else:
        print(f"Employee with the id {employee_id} was not found")
    


def create_employee():
    employee_name = input("Enter the employee name: ")
    employee_job_title = input("Enter the employee's job title: ")
    employee_department_id = input("Enter the employee's department id: ")
    try:
        employee = Employee.create(employee_name, employee_job_title, int(employee_department_id))
        print(f"Success {employee}")
    except Exception as error:
        print(f"Error in creating employee, {error}")


def update_employee():
    employee_id = int(input("Enter the employee's id: "))
    employee_name = input("Enter the employee name: ")
    employee_job_title = input("Enter the employee's job title: ")
    employee_department_id = input("Enter the employee's department id: ")

    employee = Employee.find_by_id(employee_id)
    if employee:
        try:
            employee.name = employee_name
            employee.job_title = employee_job_title
            employee.department_id = employee_department_id
            employee.update()
            print(f"Update successful: {employee}")
        except Exception as error:
            print(f"Error occured when updating, {error}")
    else:
        print(f"Employee id {employee_id} wasn't found")

def delete_employee():
    employee_id = int(input("Enter the employee's id: "))
    employee = Employee.find_by_id(employee_id)
    if employee:
        try:
            employee.delete()
            print(f"Successfully deleted employee ID {employee_id}")
        except Exception as error:
            print(f"Encountered an error during deletion, {error}")
    else:
        print(f"Couldn't find an employee with ID {employee_id}")

def list_department_employees():
    department_id = int(input("Enter the department's ID: "))
    dept_employees = Employee.department_employees(department_id)
    if dept_employees:
        for employee in dept_employees:
            print(employee)
    else:
        print(f"Employees for department with id {department_id} were not found")
