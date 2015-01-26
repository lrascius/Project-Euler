#Project Euler
#Problem 15: Lattice Paths
#Description: Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, 
#			  there are exactly 6 routes to the bottom right corner.
#			  How many such routes are there through a 20×20 grid?

import string
  
def b2s (b):
    return string.atoi(b, 2)

def max_paths(length_of_side):
    i = 0
    c = 0
    maximum = ''
    for j in range(0, length_of_side):
        maximum = '1' + maximum + '0'
    maximum = b2s(maximum)
    while i <= maximum:
        b = s2b(i)
        b = b.zfill(2 * length_of_side)
        if b.count('0') == b.count('1'):
            c += 1
        i += 1
    return c
