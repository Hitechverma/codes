class Difference:
    def __init__(self, a):
        self.__elements = a
        # print a
    # maximumDifference =None
    def computeDifference(self):
    	# self.maximumDifference =None
    	lis = []
    	for x in range(0,len(self.__elements)):
    		# print abs(self.__elements[x]-self.__elements[x-1])
    		for y in range(1,len(self.__elements)):
    			lis.append(abs(self.__elements[y]-self.__elements[x]))
    	# print lis
    	self.maximumDifference = max(lis)


# End of Difference class

_ = raw_input()
a = [int(e) for e in raw_input().split(' ')]

d = Difference(a)
d.computeDifference()

print d.maximumDifference