noc = int(input())
ml = []

def utp(n):
	c = 1
	height = 1
	while n>0:
		if c%2 ==0:
			height = height + 1
			c += 1
			n -= 1
		else:
			height = height *2
			c += 1
			n -= 1
	print height
for x in range(0,noc):
	val = int(input())
	ml.append(val)
for a in range(0,noc):
	utp(ml[a])