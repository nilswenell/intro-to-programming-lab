
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





#question 11
def add_lists(lyst1,lyst2):
    sums_list =[]
    for item in range(0,len(lyst1)):
        sums_list.append(int(lyst1[item])+int(lyst2[item]))
    print(sums_list)
add_lists([1,3,3,1],[4,3,6,1])