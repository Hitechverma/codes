no_case = int(input("Enter no. of cases:"))
def hit(line):
	string = line
	mylist = string.split(" ")
	print (mylist)
	F = int(mylist[0])
	B = int(mylist[1])
	T = int(mylist[2])
	D = int(mylist[3])

	if ( F < B):
		rel = B-F
		tot = 0	
		time = 0
		while (B < D):
			tot = tot + B + F
			D = D - rel
		time = (tot + D )*T
		print ("time taken :" ,time)

for x in range(0,no_case):
	line = input("Enter your string ")
	hit(line)