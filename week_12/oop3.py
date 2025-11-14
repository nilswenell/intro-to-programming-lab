#question 9

class ShoppingCart:
    def __init__(self,_items : dict):
        self.items = _items

    def add_item(self,item):
        if item in self.items:
            self.items[item]+=1
        else:
            self.items[item]=1

  
    def __add__(self,cart2 : dict):
        new_dict = {}
        if len(self.items)>=len(cart2):
            for key in self.items:
                if key in cart2:
                    new_dict[key]=self.items[key]+cart2[key]
                else:
                    new_dict[key]=self.items[key]
            return new_dict
        elif len(self.items)<len(cart2):
            for key in cart2:
                if key in self.items:
                    new_dict[key]=self.items[key]+cart2[key]
                else:
                    new_dict[key]=cart2[key]
            return new_dict

        
        


    def display_items(self):
        print(self.items)






cart1 = ShoppingCart({'carrot':1,'apple':2})    
cart1.add_item('celery')
cart2 = ShoppingCart({'carrot':3,'apple':2,'celery':1,'ice cream':1})   
new_cart = ShoppingCart(cart1.__add__(cart2.items))
cart1.display_items()
new_cart.display_items()