from abc import *
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
            # item.quantity=quantity
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
        

class Order:
    def __init__(self):
        self.items={}
    def addItem(self,item):
        if item in self.items:
            self.items[item] += item.quantity
        else:
            self.items[item] = item.quantity
    @property
    def totalPrice(self):
        total_price=0
        for item in self.items:
            total_price+=(item.quantity*item.price)
        return total_price

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

class Menu:
    def __init__(self):
        self.items=[]
    def addMenuItem(self,item):
        self.items.append(item)
    def findItem(self,itemName):
        for item in self.items:
            # print('in Menu class findItem method for loop')
            # print(f'item.name.lower()==itemName.lower(){item.name.lower()} {itemName.lower()}')
            if item.name.lower()==itemName.lower():
                return item
        return None
    def removeItem(self,itemName):
        item=self.findItem(itemName)
        if item:
            self.items.remove(item)
            print('Item deleted')
        else:
            print('Item not found')
    def showMenuItem(self):
        for item in self.items:
            print(f'Name: {item.name}, Price: {item.price}, Quantity: {item.quantity}')

class foodItem:
    def __init__(self,name,price,quantity):
        self.name=name
        self.price=price
        self.quantity=quantity

     
emp=Employee('Emp1','emp1@emp.com','Cape Breton','12345678912','24','Sr Engineer',2400)    
# print(emp)
Restaurant1=Restaurant('Restaurant1')
admin=Admin('Admin1','admin1@gmail.com','Cape Breton', '12345678901')
admin.addEmployee(Restaurant1,'Emp1','emp1@emp.com','Cape Breton','12345678912','24','Sr Engineer',2400)
Restaurant1.viewEmployee()
print('***************')
admin.viewEmployee(Restaurant1)
print('***************')
mn=Menu()
food=foodItem('Cappucino',5.97,10)
mn.addMenuItem(food)
mn.showMenuItem()
print('***************')
item1=foodItem('Cappucino',5,10)
item2=foodItem('Latte',4.97,10)
item3=foodItem('Americano',5,10)
admin.addNewItem(Restaurant1,item1)
admin.addNewItem(Restaurant1,item2)
admin.addNewItem(Restaurant1,item3)
Customer1=Customer('Customer1','customer1@customer.com','Cape Breton','12345678912')
Customer1.viewMenu(Restaurant1)
print('***************')
itemName=input('Enter item name:')
itemQuantity=int(input('Enter item quantity:'))
Customer1.addToCart(Restaurant1,itemName,itemQuantity)
Customer1.viewCart( )