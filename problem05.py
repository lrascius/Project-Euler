#Project Euler
#Problem 5: Smallest multiple
#Description: 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#			  What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

#Function that finds the smallest number divisible by 1 to N
def findSmallestMult(N):
	num = N
	while True:
		for i in range(2,N+1):
			if num % i != 0:
				break
			if i == N:
				return num
		num += N

print findSmallestMult(20)
