
#question 1
'''
def myfunc(word):
    otherletter = []
    for letter in range(0,len(word),2):
        otherletter.append(word[letter])
    print(otherletter)

myword = input('word:')
myfunc(myword)
'''

#question 5
'''
def hailstone(num):
    saved_values =[]
    while num != 1:
        if num%2==0:
            num/=2
        elif num%2==1:
            num= (num*3)+1
        saved_values.append(num)
            
        print(num)

hailstone(25)    
hailstone(40)
'''

#question 9

'''
def count(cards):
    cardcount = 0
    for card in cards:
        if card in range(2,7):
            cardcount+=1
        elif str(card) in ["10",'j','q','k','a']:
            cardcount-=1
    return cardcount



print(count(['a','b',9,10,3,'j','a',4,8,5]))
print(count(['a',5,5,2,6,2,3,8,9,7]))
'''


#question 11
'''
def add_lists(lyst1,lyst2):
    sums_list =[]
    for item in range(0,len(lyst1)):
        sums_list.append(int(lyst1[item])+int(lyst2[item]))
    print(sums_list)
add_lists([1,3,3,1],[4,3,6,1])
'''

#question 15
'''
def lag_days(days):
    previous_day = 0
    lags = 0
    for day in days:
        if day < previous_day:
            lags+=1
        previous_day=day
    return lags

print(lag_days([5,3,2,1]))
print(lag_days([10,11,12,9,10]))
'''

#question 17

def getindices(lyst,item):
    output = []
    for index in len(lyst):
        if lyst[index] == item:
            output.append(index) 
    return output
print(getindices([1,5,5,2,7],7))




#question 19
'''
def is_acronym(acro,lyst):
    acro2=''
    for word in lyst:
        acro2+=word[0]
    if acro == acro2:
        return True
    else:
        return False
    
print(is_acronym('abc',['apple','banana','carrot']))
print(is_acronym('ngguoy',['never','gonna','give','up','on','you']))
'''