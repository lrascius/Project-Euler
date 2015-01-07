#Project Euler
#Problem 9: Special Pythagorean triplet
#Description: A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
#
# 							  a^2 + b^2 = c^2
#
# 			  For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
#
#			  There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# 			  Find the product abc.
import math 


for a in range(0,1000):
	for b in range(0,1000):
		for c in range(0,1000):
			if(a*a+b*b == c*c and a+b+c == 1000 and a < b < c):
				print a*b*c 