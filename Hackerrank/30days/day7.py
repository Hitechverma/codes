#import sys
#n = int(raw_input().strip())
#arr = map(int,raw_input().strip().split(' '))  //Best code to split


n = input()
arr = raw_input()
mlist = (arr.split(' '))
revlist =  mlist[::-1]
# print revlist
for x in revlist:
	print x, #amazing trick to print item in a row