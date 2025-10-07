
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

'''
#question 11
def convert_knuts(knuts):
    output =''
    sickles = 0
    galleons = 0
    knuts2 = 0
    
  # if knuts >=29:
  #      sickles = knuts//29
    #    knuts2 = knuts%29
   #     if sickles >= 17:
   #         galleons = sickles//17
   #         sickles = sickles%17
            
    #option 2
    galleons = knuts//493
    knuts2 = knuts - (galleons*493)
    sickles = knuts2//29
    knuts2 = knuts2 - (sickles*29)


    if galleons > 0:
        if galleons ==1:
            output += f'{galleons} galleon, '
        else:
            output += f'{galleons} galleons, '
    if sickles > 0:
        if sickles == 1:
            output+=f'{sickles} sickle, '
        else:
            output += f'{sickles} sickles, '
    if knuts2 > 0:
        if knuts2 == 1:
            output += f'{knuts2} knut '
        else:
            output += f'{knuts2} knuts '
    
    
    #output = (f'{galleons} galleons, {sickles} sickles, and {knuts2} knuts.')
    
    
    return output
user_input = int(input('knuts: '))
print(convert_knuts(user_input))
'''

