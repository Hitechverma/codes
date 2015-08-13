noc = int(input())
list = []
fs = []

def fib(n):
	fs = []
	a , b = 1,1
	for i in range(n):
		a,b = b,a+b
		fs.append(a)
	return fs

def fab(a):
	fs = fib(a)
	org = []
	k = 0
	while fs[k] < a:
		if (fs[k]%2 == 0):
			org.append(fs[k])
			k += 1
		else:
			k+=1
	print sum(org)
	return

for x in range(0,noc):
	val = int(input())
	list.append(val)
for a in range(0,noc):
	fab(list[a])