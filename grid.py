# Counts paths to the upper right corner of a max_x by max_y grid.  For each path you may only step left or up.

# Warning don't make these values much bigger.  
max_x = 2
max_y = 2

steps = max_x + max_y # The number of steps to the corner

# Initalize current and new pathlists
pathlist = [[(0,0)]]
new_pathlist =[]

for i in range(steps):
    # We add one step to each path in the current list.
    for path in pathlist:
        last_tup = path[len(path)-1] # The last step in path.
        next_tup1 = (last_tup[0]+1,last_tup[1]) # next step right.
        next_tup2 = (last_tup[0],last_tup[1]+1) # next stop up.
        new_path1 = path + [next_tup1]
        new_path2 = path + [next_tup2]
        # Check if we have not step too far to the right.
        if (last_tup[0] + 1) <= max_x:
            new_pathlist += [new_path1]
        # Check if we have not step too far to the up.
        if (last_tup[1] + 1) <= max_y:
            new_pathlist += [new_path2]
    pathlist = new_pathlist # Make the new path the current path.
    new_pathlist =[] # Reinitialize the new path list.
# print all possible paths.
#for path in pathlist:
    #print(path)
# Count the paths and print out how many there are.
print('There are {} paths'.format(len(pathlist)))
                  



    