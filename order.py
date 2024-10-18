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
