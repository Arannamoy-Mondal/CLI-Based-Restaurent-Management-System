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
            itemQuantity=int(input("Enter item quantity:"))
            customer.addToCart(res1,itemName,itemQuantity)
        elif choice==3:
            customer.viewCart()
        elif choice==4:
            customer.payBill()
        else:
            print('Invalid choice')

def adminMenu():
    name=input("Enter name:")
    email=input("Enter email:")
    phone=input("Enter phone:")
    address=input("Enter address:")
    admin=Admin(name=name,email=email,address=address,phone=phone)
    while True:
        print(f"Welcome {admin.name}!!!")
        print(f"1. Add new item.")
        print(f"2. Add employee")
        print(f"3. View employee")
        print(f"4. View item")
        print(f"4. Remove item")
        print(f"0. Exit")
        choice=int(input("Enter your choice:"))
        if choice==0:
            break
        elif choice==1:
            name=input("Enter item name:")
            price=int(input("Enter item price:"))
            quantity=int(input("Enter item quantity:"))
            admin.addNewItem(res1,foodItem(name=name,price=price,quantity=quantity))
        elif choice==2:
            name=input("Enter employee name:")
            email=input("Enter email address:")
            address=input("Enter address:")
            phone=input("Enter phone:")
            age=input("Enter age:")
            designation=input("Enter designation:")
            salary=input("Enter salary:")
            emp=Employee(name=name,email=email,address=address,phone=phone,age=age,designation=designation,salary=salary)
            admin.addEmployee(res1,emp)
        elif choice==3:
            res1.viewEmployee()
        elif choice==4:
            admin.viewItem(res1)
        elif choice==5:
            itemName=input("Enter item name:")
            admin.removeItem(res1,itemName)
        else:
            print('Invalid choice')

while True:
    print("1. Customer")
    print("2. Admin")
    print("0. Exit")
    choice=int(input("Enter option:"))
    if choice==1:
        customerMenu()
    elif choice==2:
        adminMenu()
    elif choice==0:
        break
    else:
        print("Invalid")