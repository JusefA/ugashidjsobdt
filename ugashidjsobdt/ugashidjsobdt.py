def syt(a,b):
    if b == 0:
        return a
    else:
    	return syt(b,a%b)

print(syt(4,6))
print(syt(9,14))
print(syt(24,60))