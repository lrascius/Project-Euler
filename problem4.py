#Project Euler
#Problem 4: Largest Palindrome Product
#Description: A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99
#			  Find the largest palindrome made from the product of two 3-digit numbers.

def palindromeCheck(str):
 	temp = str[::-1]
 	if(str == temp):
 		return True
 	else:
 		return False

largestPal = 0

for i in range(0,1000):
	for j in range(0,1000):
		num = str(i*j)
		if palindromeCheck(num) == True and int(num) > int(largestPal):
			largestPal = num

print largestPal



