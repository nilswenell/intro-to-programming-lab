'''
age = int(input('whats ur age? '))

try:
    print(f'your age is {age}')
    print(f'next year you will be {age +1}')
except ValueError:
    print('pick a number!')
print('program ended normally.')
'''
'''
try:
    block of code
    #if something goes wrong 
except (code similar to statement):
    block of code 

except NameError:
    #handle type of error
    print('this is a name error.')
except ValueError:

except TypeError:
'''
'''
print('enter a number. I will divide 10 by that number and output result')
user_input = input('number: ')
try:
    user_number = int(user_input)
    result = 10 / user_number
    print(f'result: {result}')
except ValueError:
    print('gimme number')
    user_input = input('number: ')
except ZeroDivisionError:
    print('not that number')
    user_input = input('number: ')
#problems: not a number, 0, 
'''
while True:
    user_input = input("Please enter an integer: ")
    try:
        integer_value = int(user_input)
        if integer_value < 10:
            print('bigger number please.')
            continue
        print(f"You entered the integer: {integer_value}")
        break  # Exit the loop if input is a valid integer
    except ValueError:
        print("Invalid input. Please enter a whole number.")
