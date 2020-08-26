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
for j in range(1,N):
 if isPrime(j):
  if megaP.match(str(j)):
   print(j,"is a mega prime")
  else:
   print (j,"it's not a mega prime")
