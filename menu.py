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

