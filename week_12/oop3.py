#question 8

class Rectangle:

    def __init__(self,_width,_height):
        self.width = _width
        self.height = _height
    
    def get_width(self):
        return self.width
    def get_height(self):
        return self.height
    
    def get_area(self):
        return self.height * self.width
    
    def __mul__(self,number):
        return f'width: {self.get_width() * number}, height: {self.get_height() * number}'

    def __str__(self):
        return f'width: {self.get_width()}, height: {self.get_height()}'

rect1 = Rectangle(4,5)
print(rect1)
print(rect1.__mul__(3))





#question 9

class Playlist:
    def __init__(self,_name,_songs = []):
        self.name = _name
        self.songs = _songs

    def add_song(self,song):
        self.songs.append(song)
        
    def get_name(self):
        return self.name
        
    def __str__(self):
            return f'{self.get_name()} playlist: {self.songs}'
            

    def __add__(self,playlist_2):
        new_playlist = []
        for song in self.songs:
            new_playlist.append(song)
        for song in playlist_2.songs:
            new_playlist.append(song)
        return Playlist(self.get_name() + playlist_2.get_name(),new_playlist)
            
        
            
playlist_1 = Playlist('my_playlist',['song1','song2','song3'])
playlist_2 = Playlist('my_second_playlist',['song4','song5','song6'])

playlist_3 = Playlist('my_third_playlist',playlist_1.__add__(playlist_2))

print(playlist_1)
print(playlist_2)
print(playlist_3)





#question 10

class ShoppingCart:
    def __init__(self,_items = {}):
        self.items = _items

    def add_item(self,item):
        if item in self.items:
            self.items[item]+=1
        else:
            self.items[item]=1

    '''
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
            '''
    def __add__(self,other):
        combined = ShoppingCart()
        for item,qty in self.items.items():
            combined.items[item] = qty

        for item,qty in other.items.items():
            if item in combined.items:
                combined.items[item]+=qty
            else:
                combined.items[item]=qty
        return combined
        
        


    def display_items(self):
        print(self.items)






cart1 = ShoppingCart({'carrot':1,'apple':2})    
cart1.add_item('celery')
cart2 = ShoppingCart({'carrot':3,'apple':2,'celery':1,'ice cream':1})   
#new_cart = ShoppingCart(cart1.__add__(cart2.items))
new_cart = cart1 + cart2
cart1.display_items()
cart2.display_items()

new_cart.display_items()
