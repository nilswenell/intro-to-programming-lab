'''	
def convert_knuts(knuts=450):

    KNUTS_PER_SICKLE = 29
	SICKLES_PER_GALLEON = 17
	KNUTS_PER_GALLEON = KNUTS_PER_SICKLE * SICKLES_PER_GALLEON
				
	galleons = knuts // KNUTS_PER_GALLEON
	remaining_knuts = knuts % KNUTS_PER_GALLEON
				
	sickles = remaining_knuts // KNUTS_PER_SICKLE
	remaining_knuts = remaining_knuts % KNUTS_PER_SICKLE
	
	output = ""
	
	if galleons > 0:
		if galleons > 1:
			output = output + str(galleons) + " galleons"
		else:
			output = output + str(galleons) + " galleon"
	
	if sickles > 0:
		if output:
			output = output + " "
		if sickles > 1:
			output = output + str(sickles) + " sickles"
		else:
			output = output + str(sickles) + " sickle"
	
	if remaining_knuts > 0:
		if output:
			output = output + " "
		if remaining_knuts > 1:
			output = output + str(remaining_knuts) + " knuts"
		else:
			output = output + str(remaining_knuts) + " knut"
	
	return output


#print(convert_knuts(32))
print(convert_knuts())
print(convert_knuts(544))
print(convert_knuts(993))
'''


'''
def design_rug(width, length, pattern):
	result = "Your rug is:\n"
	for i in range(length):
		result += pattern * width
		if i < length - 1:
			result += "\n"
	return result

print(design_rug(3,5,'#'))


def count_duplicates(num_1, num_2, num_3):
	count = 0
	
	if num_1 == num_2:
		count += 1
	
	if num_1 == num_3:
		count += 1
	
	if num_2 == num_3:
		count += 1
	
	if count == 0:
		return "Each number is unique"
	elif count == 3:
		return "You entered the same number 3 times"
	else:
		return "You entered the same number 2 times"
	
print(count_duplicates(1,2,1))




def flip_flop(word):
	length = len(word)
	middle = length // 2

	if length % 2 == 0:
		first_half = word[:middle]
		second_half = word[middle:]
		return second_half + first_half
	else:
		first_part = word[:middle]
		middle_char = word[middle]
		last_part = word[middle+1:]
		return last_part + middle_char + first_part

print(flip_flop('cranberries'))
'''
'''
def hamming_distance(str1, str2):
	if len(str1) != len(str2):
		return "Strings must be of equal length."
	
	distance = 0
	for i in range(len(str1)):
		if str1[i] != str2[i]:
			distance += 1
	return distance
print(hamming_distance('cat', 'dog'))
'''
'''
def hailstone_seq(n):
	sequence = []
	
	while n != 1:
		sequence.append(n)
		if n % 2 == 0:
			n = n // 2
		else:
			n *=3
			n+=1
	
		
	return sequence

print(hailstone_seq(25))
'''
'''
def like_or_dislike(events):
	state = 'nothing'
	
	for event in events:
		if event == state:
			state = "nothing"
		else:
			state = event
	
	return state

print(like_or_dislike(['dislike','like','dislike']))
'''
'''
def return_unique(numbers):

	number_dicitonary = {}
	#load dictionary
	for number in numbers:
		if number in number_dicitonary:
			number_dicitonary[number] += 1			
		else:
			number_dicitonary[number] = 1

	unique_numbers = []
	#find unique numbers in dictionary
	for number in number_dicitonary:
		if number_dicitonary[number] == 1:
			unique_numbers.append(number)

	return unique_numbers

print(return_unique([1,9,8,8,7,6,1,6]))
'''

'''
def find_factors(num):
	factors = []
	
	for i in range(1, num+1):
		if num % i == 0:
			factors.append(i)

	return factors

print(find_factors(12))
'''
def palindromes(words):
    result = {"palindrome": [], "non-palindrome": []}
    
    reversed_word = ''
    for word in words:        
        #reverse the word and check if it is the orginal word
        for letter in word:
            reversed_word = letter + reversed_word
            if reversed_word == word:
                result["non-palindrome"].append(word)
            else:
                result["palindrome"].append(word)
    
    return result

print(palindromes(['madam','racecar','hello','level','python']))