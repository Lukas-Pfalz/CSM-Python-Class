# Class for Employee
# (name, ID number, department, job title)
class Employee:

    # Initial 'Employee' Object
    def __init__(self, name, ID_number, department, job_title):
        self.__name = name
        self.__ID_number = ID_number
        self.__department = department
        self.__job_title = job_title

    # Mutators for Employee Class

    def set__Name(self, name):              # Sets Name
        self.__name = name

    def set__ID_number(self, ID_number):    # Sets ID Number
        self.__ID_number = ID_number

    def set__department(self, department):  # Sets Department
        self.__department = department

    def set__job_title(self, job_title):    # Sets Job Title
        self.__job_title = job_title

    # Accessors for Employee Class

    def get__Name(self):        # returns Name
        return self.__name

    def get__ID_number(self):   # returns ID Number
        return self.__ID_number

    def get__department(self):  # returns Department
        return self.__department

    def get__job_title(self):   # returns Job Title
        return self.__job_title

    # String Object
    def __str__(self):
        return self.__ID_number + " is a " + self.__job_title + " in " + self.__department
