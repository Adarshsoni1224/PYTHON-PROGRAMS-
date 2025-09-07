x=int(input("Enter value:"))
for i in range (2,x):
	if x%i==0:
		for j in range (2,i):
			if x%j==0:
				print(i,"composite")
				break
			else:
				print(i,"prime")