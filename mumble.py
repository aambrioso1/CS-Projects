# Mumble Mumble Input Parser

def word_parse(text):
    'Breaks up text into words defined as characters separted by a space'
    low = 0  # Position of the beginning of a word
    hi = 0   # Position of the end of a word
    word_list = []
    for i in text:
        if i ==' ': # Check if we reached the end of a word
            word_list.append(text[low:hi])
            low = hi+1 # Set the start position of the next word 
        hi += 1 # Step the next character in the word
    word_list.append(text[low:len(text)]) # Put the last word on the list
    return word_list

list1 = '1 mumble 3 mumble 5'

words = word_parse(list1)
print('Here is the list of words spoken by Vesa: {}.'.format(words))
print('Vesa tried to count to {}.'.format(count))

