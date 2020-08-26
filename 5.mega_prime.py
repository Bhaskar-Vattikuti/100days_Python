import re
def isPrime(n):
    if n <= 1:
    	return False
    for i in range(2,int(n**0.5) + 1):
    	if n % i == 0:
    		return False
    return True
megaP = re.compile("[2357]+$")

N = int(input("enter a number"))

if isPrime(N):
	if megaP.match(str(N)):
		print(N)
