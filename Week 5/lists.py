#lists are sequencial datatypes like a string, but instead of letters, 
#lists can have any datatype in each spot
#list [interger, string, float, true, variable, etc.]

lyst = ['apple', 'banana', 3, False, 4.5, 'grapes']
#print(lyst[1])
#print the list portion that isnt strings

print(lyst[2:5])
newlist=[]
for item in lyst:
    if type(item) != str:
        newlist.append(item)
print(newlist)
