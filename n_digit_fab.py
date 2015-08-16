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
	fs = fib(20)
	# print fs
	count = 0
	for b in range(0,len(fs)):
		word = str(fs[b])
		# print "length" ,len(word)
		found = 0
		if len(word)==a:
			# print "ye the ans" , b+2
			found = b+2
			count += 1
			print found
			break
	return

for x in range(0,noc):
	val = int(input())
	list.append(val)
for a in range(0,noc):
	fab(list[a])