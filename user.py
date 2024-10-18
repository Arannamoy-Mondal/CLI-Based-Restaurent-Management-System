from abc import *
from footItem import *
from order import *
from menu import *
from restaurant import *
'''3 type of employee:
Customer, Employee, Admin'''
class User(ABC):
    def __init__(self,name,email,address,phone):
        super().__init__()
        self.name=name
        self.email=email
        self.address=address
        self.phone=phone

class Customer(User):
    def __init__(self, name, email, address, phone):
        super().__init__(name, email, address, phone)
        self.cart=Order()
    
    def viewMenu(self,restaurant):
        restaurant.menu.showMenuItem()

    def addToCart(self,restaurant,itemName,quantity):
        item=restaurant.menu.findItem(itemName)
        # print(itemName)
        # print(itemQuantity)
        # print(item)
        if item:
            # self.cart.append(itemName)
            if quantity>item.quantity:
                print('Item quantity exceeded !')
                return
            else:
              item.quantity=quantity
              self.cart.addItem(item)
              print('item added')
            # pass
        else:
            print('Item not found')

    def viewCart(self):
        for item,quantity in self.cart.items.items():
            print(f'Item name: {item.name}, Item price: {item.price}, Item quantity: {quantity}')
        print(f'Total price: {self.cart.totalPrice}')
        
    def payBill(self):
        print(f'Total price: {self.cart.totalPrice}.\nPayment Successful.')
        self.cart=[]


class Employee(User):
    def __init__(self, name, email, address, phone,age,designation,salary):
        super().__init__(name, email, address, phone)
        self.age=age
        self.designation=designation
        self.salary=salary
    def __repr__(self):
        return f'Name: {self.name}, Email: {self.email}, Address: {self.address}, Phone: {self.phone}, Age: {self.age}, Designation: {self.designation}, Salary: {self.salary}$'
    

class Admin(User):
    def __init__(self, name, email, address, phone):
        super().__init__(name, email, address, phone)
        self.employees=[]

    def addEmployee(self,restaurant,name, email, address, phone,age,designation,salary):
        restaurant.addEmployee(name, email, address, phone,age,designation,salary)

    def viewEmployee(self,restaurant):
        restaurant.viewEmployee()

    def addNewItem(self,restaurant,item):
        restaurant.menu.addMenuItem(item)

    def removeItem(self,restaurant,item):
        restaurant.menu.removeItem(item)
    def __repr__(self):
        return f'Name: {self.name}, Email: {self.email}, Address: {self.address}, Phone: {self.phone}'



     
