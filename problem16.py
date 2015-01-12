#Project Euler
#Problem 16: Power digit sum
#Description: 2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
#			  What is the sum of the digits of the number 2^1000?

import math

num = pow(2,1000)

result = 0

while num >= 1:
	result += num % 10
	num = num / 10

print result