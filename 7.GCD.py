a=int(input("enter a:"))
b=int(input("enter b:"))
l=[]
for j in range(2,b-1):
	if a%j==0 and b%j==0:
		l.append(j)
print (max(l))
