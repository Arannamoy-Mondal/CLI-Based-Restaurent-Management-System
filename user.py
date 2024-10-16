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

    def addNewItem(self,res,item):
        name=item.name
        price=item.price
        quantity=item.quantity
        res.menu.addItem(name,price,quantity)
# Restaurent class
class Restaurent:
    def __init__(self,name):
        self.name=name
        self.employeeList=[]
        self.menu=Menu()
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
    
    def addItem(self,name,price,quantity):
        item=Item(name,price,quantity)
        self.itemList.append(item)
        return item
    
    def showItem(self):
        for it in self.itemList:
            print(f'Name: {it.name}, Price: {it.price}$, Quantity: {it.quantity}')

    def findItem(self,item):
        for i in self.itemList:
            if item.lower()==i.name.lower():
                return i  
        return None
    
    def removeItem(self,itemName):
        item=self.findItem(itemName)
        if item:
            self.itemList.remove(item)
            print('tItem deleted')
        else:
            print('\tItem not found')


# item class
class Item:
    def __init__(self,name,price,quantity):
        self.name=name
        self.price=price
        self.quantity=quantity

# customer class

class Customer(User):
    def __init__(self, name, phone, email, address):
        super().__init__(name, phone, email, address)
        self.cart=Order()

    def UserShowItem(self,res):
        res.menu.showItem()

    def UserAddToCart(self,restaurant,item_name,quantity):
        item=restaurant.findItem(item_name)
        if item:
            item.quantity=quantity
            self.cart.addItem(item)
            print('Add successfully.')
        else:
            print('Item not found.')

    def UserViewCart(self):
        print('\tView Cart')
        print('Name\tPrice\tQuantity')
        for item,quantity in self.cart.items.items():
            print(f'{item.name}\t{item.price}\t{quantity}')
        print(f'Total Price{self.cart.totalPrice}')


# Order Class
class Order:
    def __init__(self):
        self.items={}
    
    def addItem(self,item):
        if item in self.item:
            self.items[item]+=item.quantity # if item is available in cart
        else:
            self.items[item]+=item.quantity

    def removeItem(self,item):
        if item in self.items:
            # self.items.remove(item)
            del self.items[item]     

    def totalPrice(self,item):
        return(item.price*quantity for item,quantity in self.items.items())

    def clear(self):
        self.items={}

admin1=Admin('Admin1','12345678912','admin1@admin.ca','Cape Breton, Nova Scotia')
# admin1.addEmployee('Emp1','12345678913','emp1@emp.ca','Cape Breton, Nova Scotia','35','Sr. Engineer','150K')
# admin1.viewEmployee()
menu1=Menu()
menu1.addItem('Cappuccino','5.95','20')
menu1.addItem('Latte','4.97','20')
menu1.addItem('Americano','5.95','20')
res1=Restaurent('\tWoodroad')
Customer1=Customer('Customer1','012345678912','customer1@customer.com','Cape Breton')
admin1.addNewItem(res1,Item('Cappuccino','5.95','20'))
admin1.addNewItem(res1,Item('Latte','4.97','20'))
admin1.addNewItem(res1,Item('Americano','5.95','20'))
Customer1.UserShowItem(res1)
Customer1.UserViewCart()