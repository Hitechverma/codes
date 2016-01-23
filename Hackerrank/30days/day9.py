def find_gcd(a,b):
    #write base condition
    if a == b:
    	return a
    elif (a%b) == 0:  #Very important thing to b noted 
    	return b
    else:
    	x = max(a,b) - min(a,b)
    	y = min(a,b)
    	return find_gcd(y,x%y)  #always use this return in recursion
#Take input
arr = raw_input()
mlist = (arr.split(' '))
a = int(mlist[0])
b = int(mlist[1])

gcd=find_gcd(a,b)
print gcd