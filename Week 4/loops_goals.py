
#question 1
'''
larger = int(input('larger number: '))
smaller = int(input('smaller number: '))
number = 1
while (larger/(number*2)) > smaller:
    number+=1
print(f'{larger} can be halved {number - 1} times before it isnt greater than {smaller}')
'''

#question 2
'''
word = input('word: ')
index = 1
result = ""
while index < len(word) - 1:
    result += word[index]
    index += 2

print(result)

word = input('word: ')
result = ""
for item in range(len(word)):
    if item%2==1:
        result += word[item]
print(result)
'''
#question 3
'''
number = 37
while number <= 1050:
    if number%2==0:
        print(number)
    number+=1
'''

#question 4
'''
user = ""
result = ""
while user != "done":
    user = input("enter letter or type done: ")
    if user != "done":
        result += user
print(result)
'''

#question 5

'''
number = 50
result = 0
while number <= 517:
    if number%2==1:
        result+=number
    number+=1
print(result)

total = 0
for num in range(50, 517+1):
    if num%2==1:
        total+=num
    num+=1
print(total)
'''
#question 6
number = 0
sum = 0
while number >=0:
    sum+=number
    number = int(input('number: '))
    
print(sum)
