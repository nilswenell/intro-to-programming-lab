#question 4

name_dict = {"4567": "jack", '45678':'nils', '34567':'bagel'}

def get_names(names):
    name_list = []
    for name in names:
        name_list.append(names[name])
    return name_list

#print(get_names(name_dict))


#question 5
person_dict = {'emma':71,'jack':45,'olivia':82,'liam':39}

def find_oldest(people):
    oldest = 0
    oldest_person = ''
    #find the bigest age
    for person in people:
        if people[person] > oldest:
            oldest = people[person]
            oldest_person = person
    return oldest_person

    #find the person that goes with that age
    #for person in people:
     #   if oldest == people[person]:
      #      return person
    

#print(find_oldest(person_dict))




#question 6
myword = 'asdfaasghjk'

def lettercount(word):
    dictionary = {}
    for index in range(len(word)):
        if word[index] not in dictionary:
            dictionary[word[index]]=1 
        else:
            dictionary[word[index]]+=1
    return dictionary

#print(lettercount(myword))




#question 9

receipt = {}
receipt['Side Salad'] = 6
receipt['Chicken Parm'] = 12
receipt['Cookie'] = 3

total = 0
for item in receipt:
    total +=receipt[item]
#print(total)



#question  11

animals = ['cat', 'dog', 'cat', 'cow', 'cow', 'cow']

def count_repetitions(elements):
    repetitions = {}
    for item in elements:
        if item not in repetitions:
            repetitions[item]=1
        else:
            repetitions[item]+=1
    return repetitions

#print(count_repetitions(animals))

    




#question 18




mylist = [3,3,3,4,5,6,1,1,1,1,2,2,0,5,5,5,5]

def majority_element(nums):
    num_dict = {}
    #make dictionary with number, and how many times it was in the list
    for number in nums:
        if number not in num_dict:
            num_dict[number]=1
        else:
            num_dict[number]+=1
    
    biggest = 0
    biggest_item = -1
    #find the biggest value (number of how many times)
    for item in num_dict:
        if num_dict[item] > biggest:
            biggest = num_dict[item]
            biggest_item = item
    return biggest_item

    
        
#print(majority_element(mylist))









#challenge (incomplete)
'''
namenumber = ''
challengedict ={}
while namenumber != 'quit':
    namenumber = input('name and number: ')
    words = namenumber.split(' ')
    challengedict[words[0]]=words[1]
    print(challengedict)
'''