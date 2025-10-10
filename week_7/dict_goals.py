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

    #find the bigest age
    for person in people:
        if people[person] > oldest:
            oldest = people[person]

    #find the person that goes with that age
    for person in people:
        if oldest == people[person]:
            return person
    

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

print(lettercount(myword))


