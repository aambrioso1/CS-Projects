"""
Manatees have some social heirarchy that determines their order and some insist
on a particluar position.  Need to determine the earliest that a sick manatee
can be place in the order.
"""

#  Input Data
parameters = [6, 3, 2] # 6 manatees, 3 in a given order, 2 with fixed positions
order= [4, 5, 6] # Second line of input is always the social order
fixed1 = [5,3] # This and the next line (2 lines) are the manatee and position
fixed2 = [3,1] # For example third manatee must be first in line

count = parameters[0] #  The number of manatees
order_count = parameters[1] # The length of the social hierarchy
fixed_count = parameters[2] # The number of manatees with fixed positions

# We create a list to store the current order
order_list = [0 for i in range(count)]

#  We place manatees with fixed position in the current order
fixed_list = [() for i in range(fixed_count)]
fixed_list[0] = tuple(fixed1)
fixed_list[1] = tuple(fixed2)

for i in range(fixed_count):
    num = fixed_list[i][0]
    pos = fixed_list[i][1] - 1
    order_list[pos] = num

#  Place all the manatees in a social order in the latest possible position.
"""
There are several cases:
    (1) The manatee is already in place
    (2) First manatee in the social order must be in first 0 to the left of the second.
    (3) Last manatee in order should go in the last zero.
    (4) The middle manatees must be in first zero to the next manatee and 
    to the right of the previous manatee.
    
# Finally the answer is the first 0 in the order_list
   
       