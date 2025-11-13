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

new_file.write('Name,age,thing\n')
new_file.write('Nils,19,editing\n')
new_file.write('Anders,21,cars\n')
new_file.write('Beth,49,geology\n')
new_file.write('Anthony,56,water stuff\n')

new_file.close()

my_file = open('family.txt','r')
data = my_file.readlines()
total_age = 0
how_many = 0
for line in data[1:]:
    line_data = line.split(',')
    age = line_data[1]
    total_age+=int(age)
    how_many+=1
    print(age)
print(f'avg age: {total_age/how_many}')