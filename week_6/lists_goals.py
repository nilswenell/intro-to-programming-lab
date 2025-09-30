
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




#question 8
'''
def pool_time(user_grade, user_time):
    if user_grade == 'k':
        user_grade = 0
    else: 
        user_grade = int(user_grade)
    time_output = ''
    if user_time == 'morning':
        if user_grade <= 3:
            time_output = 9
        elif user_grade <= 8:
            time_output = 10
        else:
            time_output = 11
    else:
        if user_grade <= 3:
            time_output = 1
        elif user_grade <= 8:
            time_output = 2
        else:
            time_output = 3
    print(f' time: {time_output}')

grade = input('grade: ')
time = input('morning or afternoon? ')
pool_time(grade,time)
'''

#question 11
def add_lists(lyst1,lyst2):
    sums_list =[]
    for item in range(0,len(lyst1)):
        sums_list.append(int(lyst1[item])+int(lyst2[item]))
    print(sums_list)
add_lists([1,3,3,1],[4,3,6,1])