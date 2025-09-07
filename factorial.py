"""x=int(input("Enter value:"))
i = 1
fact=1
while(i<=x):
    fact=fact*i
    i=i+1
    print("{}!={}".format(x,fact))"""

"""x=5
i=x
fact=1
while(i>1):
 fact=fact*i
 i=i-1
 print("{}!={}".format(x,fact))"""

choice=True
while choice:
    n=int(input("Enter n:"))
    fact=1   
    for i in range (1,n+1):
        fact=fact*i
        print("factorial of {}={}".format(n,fact))
        user_choice=int(input("Enter y to continue or n to stop:"))
        if user_choice=="n":
            choice=False
        else:
            choice=True