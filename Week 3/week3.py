#nils wenell

'''

# section statements fun problem



income = int(input('income: '))
status = input('married? (y/n): ')
owed = 0
rate = 0
if status == 'n':
    if income >= 44726:
        rate = .22
    elif income >= 1101:
        rate = .12
    else:
        rate = .1
else:
    if income >= 89451:
        rate = .22
    elif income >= 22001:
        rate = .12
    else:
        rate = .1
print(f'tax owed: {income * rate}')



my_var = 9
if my_var % 2 ==1:
    if my_var**3 !=27:
        my_var = my_var + 4
    else:
        my_var /= 1.5
else:
    if my_var <= 10:
        my_var *= 2
    else:
        my_var -= 2
print(my_var)



# question 8

num1 = int(input('number: '))
num2 = int(input('another: '))
num3 = int(input('one more: '))
biggest = 0
if num1 >= num2 and num1 >= num3:
    biggest = num1
elif num2 >= num3:
    biggest = num2
else:
    biggest = num3
print(biggest)



my_var = int(input('number: '))
if my_var % 2 ==1:
    if my_var**3 !=27:
        my_var = my_var + 4
    else:
        my_var /= 1.5
else:
    if my_var <= 10:
        my_var *= 2
    else:
        my_var -= 2
print(my_var)



# question 17

player_1 = input("player 1 choice: ")
player_2 = input("player 2 choice: ")
winner = ""

if player_1 == "rock":
    if player_2 == "scissors":
        winner = "player 1"
    elif player_2 == "paper":
        winner = "player 2"
    else:
        winner = "nobody"
elif player_1 == "paper":
    if player_2 == "rock":
        winner = "player 1"
    elif player_2 == "scissors":
        winner = "player 2"
    else:
        winner = "nobody"
else:
    if player_2 == "paper":
        winner = "player 1"
    elif player_2 == "rock":
        winner = "player 2"
    else:
        winner = "nobody"
print(f'{winner} wins!')

'''



    