noc = int(input())
ml = []

def dsum(n):
	add = 1
	add = 2 ** n
	kk = [] 
	kk = map(int ,str(add))
	result = sum(kk)
	print result
for x in range(0,noc):
	val = int(input())
	ml.append(val)
for a in range(0,noc):
	dsum(ml[a])