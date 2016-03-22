class Employee:
    """Base class for all employees"""

    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.count += 1

    def displayNumEmployees(self):
        print 'Total Employees:', Employee.empCount

    def displayEmployeeName(self):
        print 'Name:', self.name
