import sys

arr = []
for arr_i in xrange(6):
   arr_temp = map(int,raw_input().strip().split(' '))
   arr.append(arr_temp)
# print arr
c = 0
lis = []
for x in range(1,5):
	for y in range(1,5):
		c = arr[x][y]+arr[x-1][y]+arr[x-1][y-1]+arr[x-1][y+1]+arr[x+1][y]+arr[x+1][y-1]+arr[x+1][y+1]
		lis.append(c)
print max(lis)
