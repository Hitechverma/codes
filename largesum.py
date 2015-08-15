noc = int(input())
ml = []

for x in range(0,noc):
	val = int(input())
	ml.append(val)

s = str(sum(ml))
print s[:10]