# A program for solving the monkey tictactoe problem.


# A list of rows in the game board
row_list = ['COW', 'XXO', 'ABC']

# Other test games:  
# row_list = ['AAA', 'BBB', 'CCC']  # single winners: 3, doublewinners: 0
# row_list = ['ABA', 'BAB', 'ABA']  # single winners: 1, doublewinners: 1 
# row_list = ['AAA', 'CBC', 'CBC']  # single winners: 1, doublewinners: 3


# The string of letters use by the monkeys in the game.
string = row_list[0] + row_list[1] + row_list[2]
letterset = set(string) # Unique letters used in game.



# Each row is broken up into a list of individual letters.
bd = row_list[0] + row_list[1] + row_list[2]


# Define strings for the rows, colums and that must be checked.
row1 = bd[:3]
row2 = bd[3:6]
row3 = bd[6:]
col1 = '' + bd[0] + bd[3] + bd[6]
col2 = '' + bd[1] + bd[4] + bd[7]
col3 = '' + bd[2] + bd[5] + bd[8]
diag1 = '' + bd[0] + bd[4] + bd[8]
diag2 = '' + bd[2] + bd[4] + bd[6]

# Create a list of rows to check to use for iteration.
checklist = [row1, row2, row3, col1, col2, col3, diag1, diag2]

# Create the subsets of checklist that are wins for one monkey (singlewinnerlist) 
# or two monkeys (double winnerlist).
countlist = []
singlewinners = []
doublewinners = []
for s in checklist:
    for char in letterset:
        countlist.append(s.count(char))
        if s.count(char) == 3:
            singlewinners.append(s)
        if s.count(char) == 2:
            doublewinners.append(s)

# print(countlist)
print('Single winners: ', singlewinners)
print('Double winners: ', doublewinners)

# Create a list of the monkeys that have a win on their own (singlewinnerlist) or with a partner (doublewinnerlist).  Note that it is important  count single monkeys and teams not wims!

singlewinnerlist = []
doublewinnerlist = []
for i in singlewinners:
    k = set(i)
    if k not in singlewinnerlist:  # Only add unique single-winners to the list.
        singlewinnerlist.append(k)

for i in doublewinners:
    k = set(i)
    if k not in doublewinnerlist: # Only add unique double-winners to the list.
        doublewinnerlist.append(k)

print('Unique winner lists ', singlewinnerlist, doublewinnerlist)

print('\nThe solution is:')
print(len(singlewinnerlist))
print(len(doublewinnerlist))