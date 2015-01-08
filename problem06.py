#Project Euler
#Problem 6: Sum Square Difference
#Description: Find the difference between the sum of the squares of the first one
#			  hundred numbers and the square of the sum

def sumofSquares(num):
	return num*(num+1)*(2*num+1)/6

def squareofSum(num):
	return (num*(num+1)/2)*(num*(num+1)/2)

print squareofSum(100) - sumofSquares(100)