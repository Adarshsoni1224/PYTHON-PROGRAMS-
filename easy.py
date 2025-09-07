def fact(x):
	result=1
for i in range (1,x+1):
	result=result*i
return result

n= int(input("Enter the value:"))
r=int(input("Enter the value:"))
result+fact(n)/fact(n-r)
print("{}p{}={}".format(n,r,result))