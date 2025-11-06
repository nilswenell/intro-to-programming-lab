class Dog:
    def __init__(self,_name,_breed,_height,_weight,_color,_bark):
        self.name=_name
        self.breed=_breed
        self.height=_height
        self.weight=_weight
        self.color=_color
        self.bark=_bark

    def set_name(self,newname):
        self.name=newname
    def get_name(self):
        return self.name
    
    def set_breed(self,newbreed):
        self.breed=newbreed
    def get_breed(self):
        return self.breed
    
    def set_height(self,newheight):
        self.height=newheight
    def get_height(self):
        return self.height
    
    def set_weight(self,newweight):
        self.weight=newweight
    def get_weight(self):
        return self.weight
    
    def set_height(self,newheight):
        self.height=newheight
    def get_height(self):
        return self.height
    
    
    
    def __str__(self):
        return self.name


class DogPark:
    def __init__(self,_name):
        self.name=_name
        self.dogs=[]
    
    def add_dog(self,dog):
        self.dogs.append(dog)
    
    def show_dogs(self):
        for dog in self.dogs:
            print(dog.get_name())

    def change_dog_name(self,oldname,newname):
        for dog in self.dogs:
            if dog.get_name() == oldname:
                dog.set_name(newname)

    def find_dog(self,dog_name):
        for dog in self.dogs:
            if dog.get_name() == dog_name:
                print(f'{dog.bark}!')

    def call_dog(self,dog_name):
        index = 0
        for dog in self.dogs:
            if dog_name == dog.get_name():
                self.dogs.remove(self.dogs[index])
            index+=1


park1 = DogPark('Pibble Palace')


dog1 = Dog('Pibble','frenchy',5,4,'white','I am Pibble')

park1.add_dog(dog1)


park1.add_dog(Dog('Washingtoon','frenchy',6,5,'black','Wash my bellay'))


park1.show_dogs()

park1.change_dog_name('Washingtoon','Washington')

park1.show_dogs()

park1.find_dog('Washington')

park1.call_dog('Washington')

park1.show_dogs()
