#september 23

#determine how many letters are in a word
'''
word = 'hello world'

count = 0

for letter in word:
    if letter !=' ':
        count += 1

print(f' there are {count} letters in {word}')
'''
#determine how many vowels are in a word
'''
word_list = ['hello world', 'apples and bananas', 'happy times']
for word in word_list:
    vowels = 0
    sometimes = 0 

    for letter in word:
        if letter.lower() == 'a' or letter.lower() == 'e' or letter.lower() == 'i' or letter.lower() == 'o' or letter.lower() == 'u':
            vowels += 1
        elif letter.lower()=='y':
            sometimes+=1
    if sometimes == 0:
        print(f"there are {vowels} vowels in '{word}'")
    else:
        print(f"there are {vowels}, sometimes {vowels+sometimes} vowels in '{word}'")
'''



#definitions!
def vowel_counter(passed_word):
    count = 0
    sometimes = 0
    for letter in passed_word:
        if letter.lower() == 'a' or letter.lower() == 'e' or letter.lower() == 'i' or letter.lower() == 'o' or letter.lower() == 'u':
            count += 1
        elif letter.lower()=='y':
            sometimes+=1
    if sometimes == 0:
        print(f"there are {count} vowels in '{passed_word}'")
    else:
        print(f"there are {count}, sometimes {count+sometimes} vowels in '{passed_word}'")

word1 = 'hello world'
word2 = 'apples and bananas'
word3 = 'happy times'
vowel_counter(word1)
vowel_counter(word2)
vowel_counter(word3)

