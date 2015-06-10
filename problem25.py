#Project Euler
#Problem 25: 1000-digit Fibonacci number
#Description: The 12th term, F12, is the first term to contain three digits.
#			  What is the index of the first term in the Fibonacci sequence to contain 1000 digits?

def fibonacci(n):
	x = 1
	y = 1
	count = 2
	while len(str(y)) != n:
		temp = x 
		x = y 
		y =  temp + y
		count+=1

	return count

print fibonacci(1000)
