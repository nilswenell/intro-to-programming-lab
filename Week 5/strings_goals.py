#question 2
'''
def isfever(temp):
    output = True
    if temp[-1] == 'F':
        if int(temp[:-1])<=98.6:
            output = False
    else:    
        if int(temp[:-1])<=37:
            output = False
    return output


print(isfever('36C'))

'''

#question 4

def hamming(string1, string2):
    hammer = 0
    for letter in range(0,len(string1)):
        if string1[letter]!=string2[letter]:
            hammer +=1
    return hammer

print(hamming('asdf','asgh'))