"""Welcome to Day 8! Check out a video review of dictionaries and hashmaps here, or just jump right into the problem.

You are given a phone book that consists of your friend's names and their phone number. After that you will be given your friend's name as query. For each query, print the phone number of your friend.

Input Format

The first line will have an integer N denoting the number of entries in the phone book. Each entry consists of two lines: a name and the corresponding phone number. 

After these, there will be some queries. Each query will contain name of a friend. Read the queries until end-of-file.

Constraints
A name consists of only lower-case English letters and it may be in the format 
'first-name last-name' or in the format 'first-name'. Each phone number has exactly 8 digits without any leading zeros.

1<=N<=104
1<=queries<=104

Output Format

For each case, print  without quotes, if the friend has no entry in the phone book. Otherwise, print the friend's name and phone number. See sample output for the exact format.

To make the problem easier, we provided a portion of the code in the editor. You can either complete that code or write completely on your own.

Sample Input

3
sam
99912222
tom
11122222
harry
12299933
sam
edward
harry
Sample Output

sam=99912222
Not found
harry=12299933"""


import sys
n = input()
new_dict = {}
for x in range(0,n):
	for y in range(0,1):
		first = raw_input()
		sec = raw_input()
		new_dict[first] = sec
new_list = []
# checker = True
# while(checker):
# 	que = raw_input()
# 	if que == '':
# 		# checker = False
# 		break
# 	else:
# 		new_list.append(que)
input_str = sys.stdin.read()
new_list = input_str.split("\n")  #Most Imp things to use while accessing a file in python for input :)
# print new_dict
# print new_list
for h in new_list:
	if h in new_dict:
		print h+"="+ new_dict[h]
	else:
		print "Not found"