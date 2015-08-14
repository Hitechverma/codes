from itertools import count, takewhile
noc = int(input())
ml = []
def primes(n):
	"Generate prime numbers up to n"
	seen = list()
	for i in xrange(2, n + 1):
		if all(map(lambda prime: i % prime, seen)):
			seen.append(i)
			yield i

def smallest(n):
	result = 1
	for prime in primes(n):
		bprime = max(takewhile(lambda x:x<=n, (prime ** c for c in count(1))))
		# we could just take last instead of max()
		result *= bprime
	print result
	return result

for x in range(0,noc):
	val = int(input())
	ml.append(val)
for a in range(0,noc):
	smallest(ml[a])