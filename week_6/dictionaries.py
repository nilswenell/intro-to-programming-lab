#a dictionary organizes data as key-value pairs
#NON SEQUENCIAL
#a good example is a phone book

#example
phonebook = {'matt':5073891438, 'ashley':1234567890}
phonebook['nils'] = 6514085733

print(phonebook)

#look up a value in a dictionary
print(phonebook['nils'])   #prints just phone number

for person in phonebook.keys():      #.keys turns phonebook keys into a sequencial list
    print(person) #prints people
    print(phonebook[person]) #prints numbers
    print(person, phonebook[person]) #prints both



mywords = '''	This scene from Thelma is about a side mission that Thelma and Ben have to take, where they stop at an old friend's house in order to get a gun. This scene really reinforced how seriously Thelma is taking the main mission of getting her money back. The four stylistic elements that stood out the most to me in this scene were the use of props, wide angle shot, cross cutting, and the musical score.

The element of sound that was most impactful in forming this scene was no doubt the nondiegetic musical score. From the moment Thelma and Ben walk into Mona’s house, we hear that suspenseful music. One of the most impactful things about that score is that it has a low drum that imitates a heartbeat, which physically makes the viewer more tense. Additionally, it has that kind of high percussion that is very reminiscent of spy movies, and almost sounds like a ticking clock. The music alone shows the viewer that we’re in “mission impossible mode,” and brings a suspenseful atmosphere to the scene, but combining the music with Ben’s dialogue, the sound in this scene really brings that suspenseful feeling. 

The element of mise-en-scene that stood out to me the most in this scene was the use of props.  From the gun, to the bed, to even the roaches, the props in this scene served many purposes. The most notable prop was definitely the gun. Although we barely see it, the entire reason that they are doing what they are doing is to get this gun. As for the bed, it posed a big obstacle that Thelma had to overcome in order to get to the gun, and it even added to the spy movie theme, with thelma kind of having to do her own “stunts” to overcome it. The roaches added a bit of quality to the story, when one of them causes Thelma to drop the gun, firing it into the room below. This makes the viewer think that Mona is surely gonna notice that something is wrong, which creates suspense. When Ben simply continues with his stories, and Mona notices nothing, it creates a bit of comic relief as well.

The most important element of editing in this scene was the crosscutting. The crosscutting starts when Thelma says that she’s going to use the bathroom. Normally, this wouldn't be the sort of activity that a movie would crosscut to, but we soon realize that she’s not actually going to the bathroom, she's on a mission instead. Ben’s bland conversation with Mona alone would also be a pretty strange scene for a movie to focus on, but with the crosscutting to Thelma, the conversation becomes a sort of countdown timer. We start thinking “how long can he hold this conversation before she realizes what Thelma is up to?” Luckily, Mona is having some memory troubles with her old age, so it doesn't turn out to be a problem.

The element of cinematography that I think brought the most impact to the scene was the use of wide angle shots. There weren't that many of them, but when this technique was used, it brought a lot of value to the viewer. 
'''

def string_to_dictionary(word):
    string_as_list = word.split()
    word_dictionary = {}
    for word in string_as_list:
        if word in word_dictionary:
            word_dictionary[word] += 1
        else:
            word_dictionary[word] = 1
    return word_dictionary

print(string_to_dictionary(mywords))

'''
#another variation
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
'''