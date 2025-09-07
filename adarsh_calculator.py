# add is function dedicated for addition operation
def add(x,y) : 
	return x+y 

def sub(x,y) :
	return x-y

def mul(x,y) :
	return x*y 

def div(x,y) : 
	if y == 0 :
		print("Invalid Denominator")
	else : 
		return x/y

def check_result(m) : 
	n = int(m)
	temp = m-n 
	if temp > 0 :
		return m
	else :
		return n

#opr is function dedicated for taking user input
def opr() :
	print("=============================")
	opr1 = float(input("Enter Operand 1 : "))
	opr2 = float(input("Enter Operand 2 : ")) 
	print("=============================")
	return opr1, opr2 

#calc is the main caculator function
def calc() :
	opt_choice = input("Press 1 for Addition\nPress 2 for Substraction\nPress 3 for Divison\nPress 4 for Multiplication\nEnter a Valid Choice : ")

	if opt_choice == "1" :
		opr1, opr2 = opr()
		result = add(opr1,opr2)
		result = check_result(result)
		print("=============================")
		print("Answer : {} + {} = {}".format(opr1,opr2,result))
		print("=============================")

	elif opt_choice == "2" :
		opr1, opr2 = opr()
		result = sub(opr1,opr2)
		result = check_result(result)
		print("=============================")
		print("Answer : {} - {} = {}".format(opr1,opr2,result))
		print("=============================")

	elif opt_choice == "3" :
		opr1, opr2 = opr()
		result = div(opr1,opr2)
		result = check_result(result)
		print("=============================")
		print("Answer : {} / {} = {}".format(opr1,opr2,result))
		print("=============================")

	elif opt_choice == "4" :
		opr1, opr2 = opr()
		result = mul(opr1,opr2)
		result = check_result(result)
		print("=============================")
		print("Answer : {} * {} = {}".format(opr1,opr2,result))
		print("=============================")

	else : 
		print("Invalid Choice")
		calc()


print("=============================")
print("Welcome to Adarsh's Calculator")
print("=============================")
cont_choice = True 
while cont_choice :
	calc()
	choice2 = input("Enter Y to continue or N to Stop : ")
	if choice2 == "Y" or choice2 =="y" :
		cont_choice = True 
	else : 
		cont_choice = False
