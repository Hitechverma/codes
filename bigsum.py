n = input()
arr = raw_input()
mlist = (arr.split(" "))
s = 0
for x in range(0,n):
	s = s + int(mlist[x])
print s