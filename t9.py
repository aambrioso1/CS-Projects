from itertools import *

# List of words manatees may be trying to type with probability
word_list = ['hell 3', 'hello 4', 'idea 8', 'next 8']

#Text message that must be interpreted note that 1's are removed
texts = ['43556', '4332', '23', '6']



# Dictionary that matchings keystrokes to letters
t9 = {'2':'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}

# Creates a dictionary of words and probablities.
words = []
for item in word_list:
    words.append(item.split(' '))
word_dict = dict(words)

#Creates a list of words
word_list = [key for key in word_dict.keys()]

#Takes a string and returns all possible words manatee may be texting.
def text_word(string):
    subset = []
    for i in string:
        subset.append(t9[i])
    words = product(*subset)
    result = []
    for word in words:
        result.append(''.join(word))
    return result


# Create a list of possible [prefix, word] pairs given a text string.
def key_text(text):
    result = []
    for i in text_word(text):
        for j in word_list:
            if i == j[:len(i)]:
                result.append([i,j])
    return result

# Finds the prefix with the maximum probability
def max_word(answer_pairs):
    MAX = 0
    check = False
    for i in answer_pairs:
        if int(word_dict[i[1]]) > MAX:
            answer = i[0]
            check = True
    if check == False: 
        answer = ''
    return answer

# Iterates through each text in the list of texts and and outputs the best word.   If prefix does not appear prints a message
for text in texts:
    for i in range(len(text)):
        keys = key_text(text[:i+1])
        best_word = max_word(keys)
        if best_word != '':
            print(best_word)
        else:
            print('NOT IN DICTIONARY')
    print('')           




