class ShoppingCart:
    def __init__(self):
        self.items={}
        
    def add_item(self,item_name,price,quantity=1):
    #if item already exists then increments the quantity
        if item_name in self.items:
           self.items[item_name]['quantity']+=quantity
        else:
            self.items[item_name]={'price':price,'quantity':quantity}
        print(f"added {quantity}of {item_name}to the cart.")


    def remove_item(self,item_name,quantity=1):
        #incase you try to remove more quantity that already present
        if item_name in self.items:
            if self.items[item_name]['quantity']<=quantity:
                del self.items[item_name]
                print(f"removed all {item_name}from the cart.")
            #decrement the qty after removal
            else:
                self.items[item_name]['quantity']-=quantity
                print(f"Removed {item_name} from the cart.")
        else:
            print(f'{item_name}not found in the cart')
    def calculate_total(self):
        total_price=0
        for item in self.items.values():
            total_price+=item['price']*item['quantity']
        return total_price
    def display_cart(self):
        if not self.items:
            print("the cart is empty")
        else:
            print("shopping cart:")
            for iname, details in self.items.items():
                print(f"{iname} : {details['price']} X {details['quantity']}")
        print(f"total: {self.calculate_total()}")

#example
cart=ShoppingCart()
cart.add_item("Apple",99,5)
cart.add_item("Banana",59,3)
cart.display_cart()

cart.remove_item("apple",2)
cart.display_cart()

cart.add_item("orange",29,2)
cart.display_cart()

cart.remove_item("Banana",3)
cart.display_cart()