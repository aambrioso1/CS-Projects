# We count two things.  (1) How many letters are correct but in the wrong position.  This is r and the first number in the output.  (2) How many letters are correct but in the wrong position.  This is s and the second number output.

# Input variables.
length = 11
code = 'ABBCABBDDDC'
guess ='BACCBBABBAC'

# The set of letters in the code.  This is used to elimimate repetitions.
let = set(code)

# Initialize variables for the counting
r = 0
s = 0

# The keys of this dictionary are the letters in the code.  The values are the letter counts.

# We initialize the dictionary.
let_dict = dict(zip(let, [0 for i in range(len(let))]))

# We set up the letter counts for let_dict.
for c in code:
    let_dict[c] += 1

# We initialize a dictionary to keep track of what letters have been guessed.
guessed_let = dict(zip(let, [0 for i in range(len(let))]))

# We loop through the guessed letters and find out which ones are in the code and
# in the correct position.
for i in range(length):
    if guess[i] in code: # Is guess in code?
        if code[i] == guess[i]: # Is position correct.
            guessed_let[code[i]] += 1 # We used the letter.
            r += 1
"""
        # The code that follows needs work since letters can be repeated in the game code.
        elif guessed_let[guess[i]] < let_dict[guess[i]]: # Do we still have letters to guess.
            
            guessed_let[guess[i]] += 1 # We show that used this letter.
            s += 1
            print(guessed_let, let_dict, s)
            print(guessed_let[guess[i]], let_dict[guess[i]])
            print(i, guess[i], r, s)
"""  
# Now we look to see if any of the other letters in correct but in the wrong position.      
for i in range(length):
    if guess[i] in code and code[i] != guess[i] and guessed_let[guess[i]] < let_dict[guess[i]]:
       guessed_let[guess[i]] += 1 # We show that used this letter.
       s += 1 # Increment the count of correct letters in the wrong position

# Output the counts.          
print(r, s)
