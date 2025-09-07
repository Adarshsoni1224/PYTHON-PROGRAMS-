x=int(input("Enter start value:"))
y=int(input("Enter end value:"))
for i in range (x,y+1):
    for j in range(2,i):
        if i%j==0:
            print("{} is composite".format(i))
            break
    else:
        print("{}is prime".format(i))