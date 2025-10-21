'''
total = 0
user_number = input('enter a number or type q ')
while user_number!= 'q':
    total += int(user_number)
    user_number = input('enter a number or type q ')
print(f'total = {total}')
'''


'''
def letter_counter(word):
    letter_dictionary = {}
    for letter in word:
        if letter in letter_dictionary:
            letter_dictionary[letter]+= 1          
        else:
            letter_dictionary[letter]=1
    return letter_dictionary


my_word = 'peter piper picked a peck of pickled peppers'
print(letter_counter(my_word))
'''

def stringtolistwithvowels(word):
    words =[]
    builtword = ''
    vowelcount = 0
    for letter in word:
        if letter in 'aeiou':
            vowelcount+=1
        if letter ==' ':
            if vowelcount>=2:
                words.append(builtword)
            builtword=''
            vowelcount=0
        else:
            
            builtword+=letter
    words.append(builtword)
    return words

my_word = 'peter piper picked a peck of pickled peppers'
print(stringtolistwithvowels(my_word))