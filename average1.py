"""var_1=["Adarsh",18,75,"Indore"]
print(var_1)
print(type(var_1))
print(len (var_1))
#Read 
for i in range(len(var_1)):
    print(i)
    print(var_1[i])
#ITERATABLE
for j in var_1  :
    print   (i)
# Adding a item 
var_1.append("SONI")
print(var_1)
#Adding a specific index
var_1.insert(2,"tony")
print  (var_1   )
#Changing the element
item=18
x=var_1 .index(item)
var_1  [x]=100
print(var_1)
#Remove
var_1.remove(100)
print (var_1    )"""
 

numbers=[]
n=int(input("Enter no.interation:"))
for i in range (n):
    item=int(input("Enter value:"))
    numbers.append(item)
print(numbers)
sum=0
for j in numbers:
    sum=sum+j
Average=sum/n
print("Average of {}={}".format(numbers,Average))