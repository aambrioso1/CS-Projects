# Project #9, ASCII Clock

# A project to display times using a classical seven-segment display of given 
# times input in a 24 hour format.  The project can be found here:
# http://andrew.cs.fit.edu/~cse1002-stansifer/cse2050/projects/display/

# The variable tm should be a string in the form of time on a 24 hour clock. 
# For example 01:17, 10:39, or 20:41.

# Note we assume the input 24-hour time strings are in the correct format.
   



def clock(tm):  # tm is a string representing a time in a 24-hour format.
    if tm == 'end': 
        return print('end')
    
    # We assign each digit to a variable skipping the colon.
    n1 = int(tm[0])
    n2 = int(tm[1])
    n3 = int(tm[3])
    n4 = int(tm[4])
    
    # We assign the different single lines of five characters needed to build each number and colon for the clock display.
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
    
    # We use a loop to write the four characters of the clock and the 
    # colon together one line at a time.
    for i in range(7):
        print(chars[n1][i],' ', chars[n2][i], colon[i], chars[n3][i],' ', chars[n4][i])
        
# We check the progam by iterating over a list of times.

# A list of times.        
tm_list = ['10:28','04:20','18:28','16:39', '07:57','end']

# 
for i in tm_list: clock(i)

