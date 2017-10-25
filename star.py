inp=input("enter input: ")
for i in range(inp):
	i+=1
	print i*"*"
	while i==inp-1:
		i-=1
		print i*"*"
