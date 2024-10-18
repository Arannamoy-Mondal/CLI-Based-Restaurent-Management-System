from menu import Menu
class Restaurant:
    def __init__(self,name):
        self.name=name
        self.employees=[]
        self.menu=Menu()
    def addEmployee(self,emp):
        self.employees.append(emp)
    def viewEmployee(self):
        for employee in self.employees:
            print(employee)

