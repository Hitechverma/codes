s = 1
def fact(n):
    if n > 1:
    	global s
        s = s * n
        fact(n - 1)
    return s

noc = int(input())
ml = []

for x in range(0,noc):
	val = int(input())
	ml.append(val)
for a in range(0,noc):
	k = fact(ml[a])
	kk = [] 
	kk = map(int ,str(k))
	result = sum(kk)
	print result