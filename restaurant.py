from menu import*
from user import*
from footItem import Employee
class Restaurant:
    def __init__(self,name):
        self.name=name
        self.employees=[]
        self.menu=Menu()
    def addEmployee(self,name, email, address, phone,age,designation,salary):
        self.employees.append(Employee(name, email, address, phone,age,designation,salary))
    def viewEmployee(self):
        for employee in self.employees:
            print(employee)

