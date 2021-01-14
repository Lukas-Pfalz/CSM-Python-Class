# Name: Lukas Pfalz
# Section: CSC-1110-71762
# Date: 8/9/20
# Description: Employee Tester
# Assignment # - 7

##### Template for Assignment X, problems 1-X ######
import employee

def new_Employee(name, ID_number, department, job_title):

    # new_employee = employee.Employee("", "", "", "")
    # new_employee.set__Name(name)  # set 'Name' from array
    # new_employee.set__ID_number(ID_number)  # set 'ID Number' from array
    # new_employee.set__department(department)  # set 'Department' from array
    # new_employee.set__job_title(job_title)  # set 'Job Title' from array

    new_employee = employee.Employee(name, ID_number, department, job_title)

    return new_employee


def main():
    # Write a program that creates three Employee
    # objects to hold provided data
    name = ["Susan Meyers", "Mark Jones", "Joy Rogers"]
    ID_number = ["47899", "39119", "81774"]
    department = ["Accounting", "IT", "Manufacturing"]
    job_title = ["Vice President", "Programmer", "Engineer"]

    employee_list = []
    for num in range(3):
        new_employee = new_Employee(name[num], ID_number[num], department[num], job_title[num])

        employee_list.append(new_employee)                  # Add new employee to 'employee list'

    for employee in employee_list:
        print(employee)


# Run main program
main()
