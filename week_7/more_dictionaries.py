#write a functino that contains a dictionary containing 
#how many times each letter appears

my_word = 'peter piper picked a peck of pickled peppers'

#expected result:
#dictionary = {'p':9,'e':???}

def letter_counter(word):
    letter_dictionary = {}
    for letter in word:
        if letter in letter_dictionary:
            #find key value pair
            #increase value by 1
            letter_dictionary[letter]+=1
        else:
            #add key value pair to dictionary,
            #set value to 1
            letter_dictionary[letter]=1


    return letter_dictionary

print(letter_counter(my_word))

letter_dict = letter_counter(my_word)
for letter in letter_dict:
    print(letter, letter_dict[letter])