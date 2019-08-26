# Project 1:  How many sodas can Tom drink?

# Give the number of empty cans (e), the number found (f), and the cost in cans of a soda
# drinks(e,f,c) computes how many sodas Tom will drink.

def drinks(e,f,c):
    total = 0
    while((e + f) >= c): # Do we have enough empties?
        d = (e + f)//c # How many can Tom buy?
        f = (e + f) % c # How many leftover?
        total += d # How many did Ton drink this time?
        e = d # More empty bottle
    return total

# We run some test data
print('For 9 0 3 Tom drinks: ', drinks(9,0,3))
print('For 5 5 2 Tom drinks: ', drinks(5,5,2))
