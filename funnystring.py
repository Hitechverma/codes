import math

noc = int(input())
def funny(stri):
	rev = stri[::-1]
	mylist = (stri)
	mylistr = (rev)
	r = len(mylist)
	z = r%2
	if z == 0:
		for y in range(0,r):
			if math.fabs((ord(mylist[y]))-math.fabs(ord(mylist[y+1]))) == math.fabs((ord(mylistr[y]))-math.fabs(ord(mylistr[y+1]))):
				print "Funny"
				break
			else:
				print "Not Funny"
				break
	else:
		print "Not Funny"
list = []
for x in range(0,noc):
	stri = raw_input()
	list.append(stri)
for a in range(0,noc):
	funny(list[a])