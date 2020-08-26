def prime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            break
    else:
        return "yes"
n=int(input("enter n value:"))
i=j=1
while True:
    if prime(n-i)=="yes":
         if prime(n+j)=="yes":
            print("before prime is:",n-i)
            print("after prime is:",n+j)
            break
         else:
            j=j+1
    else:
        i=i+1
