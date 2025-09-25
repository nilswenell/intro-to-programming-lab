#some functions are in strings.py!

#write a function that adds 2, then multiplies by 4

#define functions up top
def twofour(number):
    number = (number + 2) * 4
    return number

def add10(number):
    number +=10
    return number
'''
print(twofour(10))

#call functions throughout the code

#function inside a function ???
print(twofour(twofour(10)))
print(add10(twofour(4)))

#call the function 10 times, 100 times
x = 0
temp = 10
while x < 100:
    temp = twofour(temp)
    x+=1
print(temp)
'''
#write a function that returns the product of two arguments

def product(num1, num2):
    return num1*num2
#call
print(product(3,4))
print(product(10,product(3,4)))