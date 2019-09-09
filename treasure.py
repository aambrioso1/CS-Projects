import itertools as it

map1 = [[1,4,7], [2,5,8], [9,6,3], [1,5,9]]

"""
map1 = [[1,4,7], [2,5,8], [9,6,3], [1,5,9], [1,2,3], [1,4,7], [2,5,8], [9,6,3], [1,5,9], [1,2,3]]
"""
# Creates all possible collections routes including collecting the
# same treasure at successive islands.  The product function produces the 
# cartesian product.  For documentation visit https://docs.python.org/3/library/itertools.html#itertools.product
 
routes = it.product(range(3), repeat=len(map1))

# Removes all routes that collect the same treasure at successive islands
goodroutes=[]
for i in routes:
    check=[]
    for j in range(len(i)-1):
        if i[j] != i[j+1]:
            check.append(True)
        else: 
            check.append(False)          
    if False not in check:
        goodroutes.append(i)

# Creates a list of all the sums for the routes in goodroutes.
sumlist =[]                    
for i in range(len(goodroutes)):
    sum = 0
    for j in range(len(goodroutes[0])):
        sum += map1[j][goodroutes[i][j]]
    sumlist.append(sum)

# Prints the list of sums and then the maximum value in that list.
print(sumlist)
print('**********************************************')
print('The maximum value that can be collected is: {}'.format(max(sumlist))) 
print('**********************************************')

  

