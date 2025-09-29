def circle():
	r=int(input("Enter radius of circle:"))
	a=r*r*(22/7)
	c=r*2*(22/7)
print("Area of circle with radius{}={}".format(r,a))
print("circumference of circle{}={}".format(r,c))

for i in range(25):
	circle()