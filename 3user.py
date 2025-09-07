a=int(input("Enter values a :"))
b=int(input("Enter values b :"))
c=int(input("Enter values c :"))
d=int(input("Enter values d :"))

if a>b and a>c and a>d:
	print("a is greatest")
elif b>a and b>c and b>d:
	print("b is greatest")
elif c>a and c>b and c>d:
	print("c is greatest")
else:
	print("d is greatest")
