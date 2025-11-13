'''
#program that takes ints from user, adds them together
#until type 'q'
sum = 0
x = input('number: ')
while x != 'q':
    y = float(x)
    sum += y
    x = input('number: ')
print(sum)
'''
'''
from random import randint
my_file = open('numbers.txt','w')

for index in range(0,100):
    number = randint(50,250)
    my_file.write(str(number)+'\n')

my_file.close()
'''
'''

my_file = open('numbers.txt','r')
data = my_file.readlines()
print(data)

total = 0
count = 0
for item in data:
    total += int(item)
    count += 1
print(f' average: {total/count}')
'''

new_file = open('family.txt','w')

new_file.write('Nils')
new_file.write('Anders')
new_file.write('Beth')
new_file.write('Anthony')

new_file.close()