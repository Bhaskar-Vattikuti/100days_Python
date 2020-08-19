n = int(input())
i = 2
while i< int(n**0.5)+1:
	if not n % i:
		print(" Its Not Prime ")
		break
	i += 1
else:
	print(" Its a Prime") 
