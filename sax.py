# A program to count the number key presses on a Sax given the notes of a song.

"""
Fingerings for notes on a Saxaphone
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
a = {2,3,4,7,8,9,10}
b = {2}
C = {3}
D = {1,2,3,4,7,8,9}
E = {1,2,3,4,7,8}
F = {1,2,3,4,7}
G = {1,2,3,4}
A = {1,2,3}
B = {1,2}

song = 'cdefgab'
song2 = 'CbCaDCbCbCCbCbabCCbCbabae'
fingerbins = []
finger_dict = dict(zip('cdefgabCDEFGAB', [c,d,e,f,g,a,b,C,D,E,F,G,A,B]))
                                         
for i in range(0,10):
    fingerbins.append(0)
# Count finger presses for the first note
firstnote = song2[0]
for i in finger_dict[firstnote]:
    fingerbins[i-1] += 1
print(fingerbins)
# Now we need to count the rest of the key presses.   Since the fingerings are 
# listed as sets, we can use set difference to figure out which keys were pressed.
# Then increment the appropriate bins.  For example if e presesed after we compute
# e - G = {2,3,4,7,8} - {1,2,3,4} = {7, 8}  
# so the bins for 7 and 8 should be each be incremented by 1.
    
