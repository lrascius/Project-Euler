#Project Euler
#Problem 7: 10001st prime
#Description: By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
#			  What is the 10 001st prime number?

primes = []
primes.append(2)
i = 2
while len(primes) < 10001:
	i+=1
	for j in range(0, len(primes)):
		if(i % primes[j] == 0):
			break;
		if(j == len(primes)-1):
			primes.append(i)

print primes[10000]