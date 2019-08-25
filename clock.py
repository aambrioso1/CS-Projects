# Project #9, ASCII Clock

# The project can be found here:
# http://andrew.cs.fit.edu/~cse1002-stansifer/cse2050/projects/display/

# Note we do not check if the time makes sense.
# And, we only handle one time at a time.   

# We assign the time to the variable tm
tm = '23:58'

# We assign each digit to a variable.
n1 = int(tm[0])
n2 = int(tm[1])
n3 = int(tm[3])
n4 = int(tm[4])

# We assign the different single lines of five characters each needed to build numbers and colon for the clock
l ='+---+'    # line
sd ='|   |'   # sides
sp='+   +'    # side plusses
d = '  o  '   # dot
lp = '|    '  # left pipe
rp = '    |'  # right pipe
rpl = '    +' # right plus
e = '     '   # empty

# We define each of the numbers and the colon as lists of the line types.
colon = [e,e,d,e,d,e,e]
zero = [l, sd,sd,sp,sd, sd, l]
one = [rpl, rp, rp, rpl, rp, rp, rpl]
two = [l,rp, rp, l, lp, lp,l]
three = [l,rp, rp, l, rp, rp,l]
four = [sp, sd, sd, l, rp, rp, rpl]
five = [l, lp,lp,l,rp,rp,l]
six = [l, lp,lp,l,sd,sd,l]
seven = [l, rp,rp,rpl,rp,rp,rpl]
eight = [l, sd,sd,l,sd,sd,l]
nine = [l, sd,sd,l,rp,rp,l]

# chars is a list of the clock character definitions
chars = [zero, one, two, three, four, five, six, seven, eight, nine]

# We use a loop to write the four characters of the clock and the colon together one line at a time.
for i in range(7):
    print(chars[n1][i],' ', chars[n2][i], colon[i], chars[n3][i],' ', chars[n4][i])