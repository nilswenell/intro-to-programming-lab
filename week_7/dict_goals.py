#question 4

name_dict = {"4567": "jack", '45678':'nils', '34567':'bagel'}

def get_names(names):
    name_list = []
    for name in names:
        name_list.append(names[name])
    return name_list

print(get_names(name_dict))