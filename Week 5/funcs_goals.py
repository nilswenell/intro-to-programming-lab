#question 11
def convert_knuts(knuts):
    output =''
    sickles = 0
    galleons = 0
    knuts2 = 0
    '''
    if knuts >=29:
        sickles = knuts//29
        knuts2 = knuts%29
        if sickles >= 17:
            galleons = sickles//17
            sickles = sickles%17
            '''
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