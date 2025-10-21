#question 1
'''
def toss_coin(guess):
    from random import randint
    value = randint(0,1)
    if guess == value:
        return "correct!"
    else:
        "incorrect!"
'''
#print(toss_coin(1))




#question 7


def ascending_order(num1,num2=15,num3=5):
    lyst=[num1,num2,num3]
    if lyst[0]>lyst[1]:
        lyst[0],lyst[1]=lyst[1],lyst[0]
    if lyst[0]>lyst[2]:
        lyst[0],lyst[2]=lyst[2],lyst[0]
    if lyst[1]>lyst[2]:
        lyst[1],lyst[2]=lyst[2],lyst[1]
    return lyst

#print(ascending_order(40,15,5))


#question 15
def is_negative(number):
    if number<0:
        return True
    else:
        return False
    
def is_odd(number):
    if number%2==1:
        return True
    else:
        return False
    
def report_negative_odds(int_list):
    negative_odd_list=[]
    for number in int_list:
        if is_odd(number) and is_negative(number):
            negative_odd_list.append(number)
    return negative_odd_list

print(report_negative_odds([100,24,-1,-567,56,-22]))





#CHALLENGE

def calc_toll(hour,am,weekend):
    toll = 0.0

    if weekend == False:
        if am == True:
            if hour<7:
                toll=1.15
            elif hour<10:
                toll=2.95
            else:
                toll=1.9
        else:
            if hour<3:
                toll=1.9
            elif hour<8:
                toll=3.95
            else:
                toll=1.1
    else:        
        if am == True:
            if hour<7:
                toll=1.05
            else:
                toll=2.15
        else:
            if hour<8:
                toll=2.15
            
            else:
                toll=1.1
    return toll