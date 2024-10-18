from footItem import*
from menu import*
from order import*
from restaurant import*
from user import*
# emp=Employee('Emp1','emp1@emp.com','Cape Breton','12345678912','24','Sr Engineer',2400)    
# # print(emp)
# Restaurant1=Restaurant('Restaurant1')
# admin=Admin('Admin1','admin1@gmail.com','Cape Breton', '12345678901')
# admin.addEmployee(Restaurant1,'Emp1','emp1@emp.com','Cape Breton','12345678912','24','Sr Engineer',2400)
# Restaurant1.viewEmployee()
# print('***************')
# admin.viewEmployee(Restaurant1)
# print('***************')
# mn=Menu()
# food=foodItem('Cappucino',5.97,10)
# mn.addMenuItem(food)
# mn.showMenuItem()
# print('***************')
# item1=foodItem('Cappucino',5,10)
# item2=foodItem('Latte',4.97,10)
# item3=foodItem('Americano',5,10)
# admin.addNewItem(Restaurant1,item1)
# admin.addNewItem(Restaurant1,item2)
# admin.addNewItem(Restaurant1,item3)
# Customer1=Customer('Customer1','customer1@customer.com','Cape Breton','12345678912')
# Customer1.viewMenu(Restaurant1)
# print('***************')
# itemName=input('Enter item name:')
# itemQuantity=int(input('Enter item quantity:'))
# Customer1.addToCart(Restaurant1,itemName,itemQuantity)
# Customer1.viewCart( )
res1=Restaurant('Woodroad')
def customerMenu():
    name=input("Enter name:")
    email=input("Enter email:")
    phone=input("Enter phone:")
    address=input("Enter address:")
    customer=Customer(name=name,email=email,address=address,phone=phone)
    while True:
        print(f"Welcome {customer.name}!!!")
        print(f"1. View Menu")
        print(f"2. Add item to cart")
        print(f"3. View Cart")
        print(f"4. Pay Bill")
        print(f"0. Exit")
        choice=int(input("Enter your choice:"))
        if choice==0:
            break
        elif choice==1:
            customer.viewMenu(res1)
        elif choice==2:
            itemName=input("Enter item name:")
            itemQuantity=input("Enter item quantity:")
            customer.addToCart(res1,itemName,itemQuantity)
        elif choice==3:
            customer.viewCart()
        elif choice==4:
            customer.payBill()

