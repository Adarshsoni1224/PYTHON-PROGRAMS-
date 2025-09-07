n=int(input("enter the value:"))
r=int(input("enter the value:"))
fact_n=1
for i in range (1,n+1):
	fact_n=fact_n*1
fact_nr=1
for j in range(1,(n-r)+1):
	fact_nr=fact_nr*j
npr=fact_n/fact_nr
print("{}p{}={}".format(n,r,npr))