# A program to count the number key presses on a Sax given the notes of a song.

"""
Fingerings for notes on a Saxaphone:
c: finger 2-4, 7-10
d: finger 2-4, 7-9
e: finger 2-4, 7, 8
f: finger 2-4, 7
g: finger 2-4
a: finger 2, 3
b: finger 2
C: finger 3
D: finger 1-4, 7-9
E: finger 1-4, 7, 8
F: finger 1-4, 7
G: finger 1-4
A: finger 1-3
B: finger 1-2
"""

c = {2,3,4,7,8,9,10}
d = {2,3,4,7,8,9}
e = {2,3,4,7,8}
f = {2,3,4,7}
g = {2,3,4}
a = {2,3}
b = {2}
C = {3}
D = {1,2,3,4,7,8,9}
E = {1,2,3,4,7,8}
F = {1,2,3,4,7}
G = {1,2,3,4}
A = {1,2,3}
B = {1,2}

" A list of songs to use for testing the program"
# song = '' # Empty song will crash the program.  Need a solution.
# song = 'cdefgab'
# song = 'BAGFEDC'
song = 'CbCaDCbCbCCbCbabCCbCbabae'

# A dictionary with the keys being notes and the values sets of fingers that must be pressed for each note.
finger_dict = dict(zip('cdefgabCDEFGAB', [c,d,e,f,g,a,b,C,D,E,F,G,A,B]))

# A list of lists (bins) to keep track of how many times each finger is pressed.
finger_bins = []                                        
for i in range(0,10):
    finger_bins.append(0)
    

# Count finger presses for the first note
if len(song) > 0:
    firstnote = song[0]
# else:
    # Need code to handle an empty song
    # Simplest solution is:  return 0 0 0 0 0 0 0 0 0 0
    

for i in finger_dict[firstnote]:
    finger_bins[i-1] += 1
print(finger_bins)
# Now we need to count the rest of the key presses.   Since the fingerings are listed as sets, we can use set difference to figure out which keys were pressed.
# Then increment the appropriate bins.  For example if e presesed after we compute
# e - G = {2,3,4,7,8} - {1,2,3,4} = {7, 8}  
# so the bins for 7 and 8 should be each be incremented by 1.

# Uses set difference to compute what notes were pressed.   
for i in range(len(song)-1):
    note = song[i] # current note
    nextnote = song[i+1] # next note played
    # set of fingers pressed in transition
    fingers_pressed = finger_dict[nextnote] - finger_dict[note]
    # These print statements are here to help the reader in understand the code.
    print('Note {}'.format(note), "followed by note {}".format(nextnote))
    print('The fingers pressed are {}'.format(fingers_pressed))
    # This loop counts how many times each note was pressed add increments the bins.
    for i in fingers_pressed:
        finger_bins[i-1] += 1

finger_string = ''
for i in finger_bins:
    finger_string += ' ' + str(i)
print(finger_string)

# Output the list
print('\n\n***************************************')
print('Counts: {}'.format(finger_string))
print('***************************************')
    