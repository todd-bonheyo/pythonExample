class VendingMachine:
    def __init__(self, num):
        self.count = num
        self.max = num

    def refill(self): 
        self.count = self.max
        print('Refilled')
    def sell(self, order):
        self.count -= order
        print('Sold:', order)
    def print_stock(self): 
        print('Current stock:', self.count)

    def __str__(self):
        return "Give me my coffee"

stock = int(input("Enter current stock: "))
vm = VendingMachine(stock)
vm.print_stock()
order_1 = int(input("Enter order: "))
vm.sell(order_1)
vm.print_stock()
vm.refill()
vm.print_stock()
print(vm)

#Comment as an example
print(vm)
