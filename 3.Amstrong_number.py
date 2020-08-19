n=input()
l=[]
for i in n:
    i=int(i)
    i=i*i*i
    l.append(i)
if int(n)==sum(l):
    print("its an amstrong number")
else:
    print("its not an amstrong number")
    
