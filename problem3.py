#Project Euler 
#Problem 3: Largest Prime Factor
#Description: The prime factors of 13195 are 5, 7, 13 and 29.
#			  What is the largest prime factor of the number 600851475143 ?

num = 600851475143 

primeFactors = 1
div = 2

while num > 1:
	while num % div == 0:
		primeFact = div
		num/=primeFact
	div+=1	
	if div*div > num:
		primeFact = num
		break 

print primeFact
