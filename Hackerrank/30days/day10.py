def see(nu):
	conversion(nu)
	print ("")

def conversion(num):
	if num>1:
		conversion(num//2)
	print (num%2,end='')

# num = input()
# conversion(num)
n = int(input())
mlist = []
for x in range(0,n):
	val = int(input())
	mlist.append(val)

for a in range(0,n):
	see(mlist[a])