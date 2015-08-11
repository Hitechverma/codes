noc = int(input("test case"))
def funny(stri):
	mylist = (stri)
	r = len(mylist)/2
	for y in range(0,r):
		if ord(mylist[r-y])-ord(mylist[y]):
			print "yes"

for x in range(0,noc):
	stri = raw_input("string")
	funny(stri)