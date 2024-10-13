'''
3 type user:
Customer
Employee
Admin
'''
from abc import ABC

# Common class for every user
class User(ABC):
    def __init__(self,name,phone,email,address):
        self.name=name
        self.phone=phone
        self.email=email
        self.address=address
        super().__init__()
# Employee class
class Employee(User):
    def __init__(self, name, phone, email, address,age,designation,salary):
        super().__init__(name, phone, email, address) # using inheritance
        self.age=age
        self.designation=designation
        self.salary=salary

class Admin(User):
    def __init__(self, name, phone, email, address,):
        super().__init__(name, phone, email, address)

    def addEmployee(self,restaurent,employee):
         restaurent.addEmployee(employee)
         print(f'\n\tEmployee add successfully.')
    
    def viewEmployee(self,restaurent):
        restaurent.viewEmployee()


# Restaurent class
class Restaurent:
    def __init__(self,name):
        self.name=name
        self.employeeList=[]
        
    def addEmployee(self,employee):
         self.employeeList.append(employee)
         print(f'\n\tEmployee add successfully.')   

    def viewEmployee(self):
        for i in self.employeeList:
            print(f'\n\tName: {i.name}, Phone: {i.phone}, Email: {i.email}, Address: {i.address}, Age: {i.age}, Salary: {i.salary}$')


# Menu Class
class Menu:
    def __init__(self):
        self.itemList=[]
    
    def addItem(self,item):
        self.itemList.append(item)
    
    def showItem(self):
        print(self.itemList)

    def findItem(self,item):
        for i in self.itemList:
            if item.lower()==i.name.lower():
                return i
        return None
    
    def removeItem(self,itemName):
        item=self.findItem(itemName)
        if item:
            self.itemList.remove(item)
            print('Item deleted')
        else:
            print('Item not found')
# admin1=Admin('Admin1','12345678912','admin1@admin.ca','Cape Breton, Nova Scotia')
# admin1.addEmployee('Emp1','12345678913','emp1@emp.ca','Cape Breton, Nova Scotia','35','Sr. Engineer','150K')
# admin1.viewEmployee()
res1=Restaurent('Woodroad')