n = int(input("in:"))
s = 1


def fact(n):
    if n > 1:
    	global s
        s = s * n
        fact(n - 1)
    return s


fact(n)
print s
