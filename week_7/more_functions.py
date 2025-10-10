# a function is a data type!

# two operators. assignment =, and invoking ().
'''
def add_three(x):
    y = x + 3
    return y

variable_zero = 7

variable_one = add_three(variable_zero)
'''

# we write code in the "(__main__)" which is inside of "(__builtin__)".
# __builtin__ includes functions  like print and datatypes like str.

# when a function is invoked, python creates a local 
# namespace corresoponding to the function itself.

# similar to how __main__ is inside of __builtin__, 
# the new namespace (add_three) is inside of __main__.


#when the function is completed, the local namespace is DESTROYED!!!! (garbage collection)

'''
print(y)
'''

#this is an error because y only existed in a namespace that was deleted.

import math

x = math.sqrt(16)
print(x)


from math import sqrt

y = sqrt(16)
print(y)



import more_dictionaries
#help(more_dictionaries)

import math as silly_stuff

print(silly_stuff.pi)