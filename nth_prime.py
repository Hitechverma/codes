from itertools import count, takewhile

def primes(n):
	"Generate prime numbers up to n"
	seen = list()
	su = 0
	for i in xrange(2, n + 1):
		if all(map(lambda prime: i % prime, seen)):
			seen.append(i)
	print seen
	print seen[-1:]
noc = int(input())
ml = []

for x in range(0,noc):
	val = int(input())
	ml.append(val)
for a in range(0,noc):
	primes(ml[a])