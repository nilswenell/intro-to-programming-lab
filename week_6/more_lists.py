    #list
weekdays = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday']

    #print item
#print(x[2])

    #slicing
#print(x[1:4])

    #print items in list 1 by 1
#for day in weekdays:
#    print(day)

    #append adds to list
#weekdays.append('saturday')
#weekdays.append('sunday')

    #slicing of specific item
#print(weekdays[2][3:6])

    #change an item
#weekdays[4]='funday'
    #friday is now funday
#print(weekdays)


    #lists are mutable, which means they can actually be changed

#x = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday']
#y = x

#print(x)
#print(y)

#x[4]= 'funday'

#y changes to new list as well (this doesnt happen with strings because theyre immutable)
#print(x)
#print(y)


    # a tuple is an immutable list

    #they use parentheses instead of brackets
workdays = ('monday', 'tuesday', 'wednesday', 'thursday', 'friday')

#print(workdays)

    #this doesnt work because its a tuple
#workdays[4] = 'funday'
#print(workdays)




#write a function that takes a string as an 
#argument and returns a list of all the words in that string.
myword = 'peter piper picked a peck of pickled peppers.'
'''
#how i did it (not fully correct)
def listmaker(string):
    list = []
    startpoint = 0
    endpoint = 0
    for number in range(len(string)):
        if string[number] == ' ' or string[number]=='.':
            endpoint = number
            list.append(string[startpoint:endpoint])
            startpoint = endpoint
    print(list)        
listmaker(myword)


#how he did it
def stringtolist(word):
    words = []
    built_word= ''
    for letter in word:
        if letter == ' ':
            words.append(built_word)
            built_word=''
        else:
            built_word += letter
    words.append(built_word)
    return words

print(stringtolist(myword))

'''

#write a function that takes a string as an argument, and returns a list 
#containing all of the words that have at least two vowels.

def twovowels(word):
    words=[]
    builtword=''
    vowelcount = 0
    for letter in word:

        if letter == ' ':
            if vowelcount >= 2:
                words.append(builtword)
            builtword=''
            vowelcount=0
        else:
            builtword += letter
            if letter in 'aeiou':
            # ^^^ same as 
            #if letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u' 
                vowelcount+=1
        #debug tool 
        #print(letter, vowelcount, builtword)
    if vowelcount >= 2:
        words.append(builtword)        
    return words
print(twovowels(myword))



def uniquewords(word):
    words = []
    built_word= ''
    for letter in word:
        if letter == ' ':
            if built_word not in words:
                words.append(built_word)
            built_word=''
        else:
            built_word += letter
    if built_word not in words:
        words.append(built_word)
    return words

print(uniquewords('peter peter piper picked peter a peck of peter'))
