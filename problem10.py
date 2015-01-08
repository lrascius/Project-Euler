#Project Euler
#Problem 10: Summation of primes
#Description: The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

#			  Find the sum of all the primes below two million.


primes = []
primes.append(2)
primes.append(3)

i = 3
while i < 2000000:
	i+=2
	for j in range(0, len(primes)):
		if(i % primes[j] == 0 or i > 2000000):
			break;
		if(j == len(primes)-1):
			primes.append(i)

print sum(primes)