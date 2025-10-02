
#for loops

#print numbers 1-10

'''
for number in range(1,10+1):
    print(number)
'''

#print all even numbers 1-10

'''
for number in range(1,11):
    if number%2==0:
        print(number)

for number in range(2,11,2):
    print(number)
'''

#print all odd numbers from 5 to a user given number
'''
user_number = int(input('number:'))
for number in range(5,user_number+1):
    if number%2==1:
        print(number)
'''
#find the sum of user entered values until the user types q
#for loops kinda suck for indeterminate times

'''
var = "hello world"

#slicing
print(var[2:8])

#iterating
for item in var:
    print(item)
'''
