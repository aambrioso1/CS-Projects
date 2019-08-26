# A solution to Project #1, Reversing numbers.
# The project was found here: http://andrew.cs.fit.edu/~cse1002-stansifer/cse2050/projects/reverse/


# This function reverse a string.
def reverse(string): 
    string = string[::-1]  # Slice string from one end to the other backward
    return string

# This functions uses reverse to convert a decimal to the decimal that results if
# the binary represenation of the decimal were reverse and converted to decimal
def reverse_bin(n):
    bin_num = bin(n)[2:] # convert a n to string of the binary digits with '0b' 
    bin_str = reverse(bin_num) # Reverse bin_num
    return int(bin_str,2) # Converts the string of binary digits to decimal

# We set up a test list to check if it works.
test_list = [1, 13, 11, 47, 61, 1000, 10000000]

# We test reverse_bin() on the values in our list.
for i in test_list:
    print(reverse_bin(i))

