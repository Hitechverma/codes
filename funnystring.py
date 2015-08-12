noc = int(input())
def funny(stri):
	mylist = (stri)
	r = len(mylist)/2
	for y in range(0,r-1):
		if (ord(mylist[r-y])-ord(mylist[y]) == ord(mylist[r-y-1])-ord(mylist[y+1])):
			print "funny"
			break
		# else:
		# 	print "not funny"
		# 	break
list = []
for x in range(0,noc):
	stri = raw_input()
	rev = stri[::-1]
	print rev
	list.append(stri)
for a in range(0,noc):
	funny(list[a])