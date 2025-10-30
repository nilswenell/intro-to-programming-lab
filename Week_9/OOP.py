'''
# OOP: Object Oriented Programming
# every data object is an item in python.

# classes describe what an object looks like.
# example: int. the number 3 would be an instance of the 'int' class.
# one of the things this class can do is undergo operations.

x = 3 # x is an instance of an int
x = x + 3 # this int did an operation by adding 3
#     ^ this '+' is an alias for x.__add__(3) or something.

# if i told x to do something like calling an index
# print(x[1])
# it would give me an error because the int class doesnt know how to do that. 


#formatting a class

#class Classname:                this is like calling a dog a dog.
#   def method1():               this is like describing what a dog can do.
#       block of code
#   def method2():
#       block of code            all methods are functions, not all functions are methods.



#constructors define the way the object is created
# __init__()

# all methods require one special parameter which 
# refers to the object being created.
'''


#lets make a planet class that has
#name
#radius
#mass
#distance

import math

class Planet:

    def __init__(self,_name,_radius,_mass,_distance):
        self.name = _name
        self.radius = _radius
        self.mass = _mass
        self.distance = _distance

    def get_name(self):
        return self.name
    
    def get_radius(self):
        return self.radius
    
    def get_mass(self):
        return self.mass
   
    def get_distance(self):
        return self.distance
    
    def get_volume(self):
        volume = 4/3 * math.pi * self.radius **3
        return volume
    
    def get_density(self):
        density = self.mass / self.get_volume()
        return density
    
    #mutator methods/setters

    def set_name(self,new_name):
        self.name = new_name

    
    def __str__(self):
        msg = ''
        msg += f'Hello {self.get_name()}. How are you?'
        return msg
    


planet1 = Planet("bagel planet", 500, 600, 1200)

#print(planet1)


#changing planet attribute (name)
#print(planet1.get_name())
#planet1.set_name('donut planet')
#print(planet1.get_name())





'''
print(planet1.get_name())
print(planet1.get_radius())
print(planet1.get_mass())
print(planet1.get_distance())
print(planet1.get_volume())
print(planet1.get_density())
'''












#dog class


class Dog:
    def __init__(self,_name,_size,_breed,_color):
        self.dogname = _name
        self.color = _color
        self.size = _size
        self.breed = _breed

    def get_name(self):
        return self.dogname

    
dog1 = Dog('bagel', 15, 'beagle', 'red')
#print(dog1.get_name())



    

    


class Star:
    def __init__(self, _name):
        self.name = _name
    
    def get_name(self):
        return self.name
    
    def set_name(self,new_name):
        self.name = new_name

    def __str__(self):
        msg = ''
        msg += f"I am {self.get_name()}, I'm a star!!"
        return msg


awesome_star = Star('Awesome Star')

print(awesome_star)