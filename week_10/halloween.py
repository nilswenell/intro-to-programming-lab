class Candy:

    def __init__(self):
        self.name = 'unknown'
        self.size = 'unknown'
        self.flavor = 'unknown'
        self.shape = 'unknown'
        self.price = 0

    def get_name(self):
        return self.name
    def set_name(self,new_name):
        self.name = new_name

    def get_price(self):
        return self.price
    def get_price_cad(self):
        return self.price * 1.4
    def set_price(self,new_price):
        if 0 <= new_price < 1000:
            self.price = new_price
    
    def get_shape(self):
        return self.shape
    def set_shape(self,new_shape):
        self.shape = new_shape
    
    def get_size(self):
        return self.size
    def set_size(self,new_size):
        self.size = new_size

    def get_flavor(self):
        return self.flavor
    def set_flavor(self,new_flavor):
        self.flavor = new_flavor


    def reaction(self):
        if 0<self.size<5:
            return "too small!!"
        if 5<self.size<10:
            return "decent size"
        else:
            return "wowza!!!!"

    def __str__(self):
        return f'{self.name}: it is {self.flavor} flavored, it costs {self.price} ({self.get_price_cad()} cad), its shape is {self.shape}, and it is {self.size}. {self.reaction()}'
    
candy1 = Candy()
candy1.set_name("KitKat")
candy1.set_shape('rectangle')
candy1.set_size(10)
candy1.set_price(499.99)
candy1.set_flavor('chocolate')

bag_of_candies = [candy1]

for candy in bag_of_candies:
    print(candy1)