def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

def calculator():
    print("Select operation:")
    print("1. add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

choice=int(input("Enter choice(1,2,3,4):"))

if choice in  ["1","2","3","4"]:
    num1 = input("Enter the first value:")
    num2 = input("Enter the second value:")

    if choice == ("1") :
         result==add(num1,num2)
        elif choice==("2"):
            result==Subtract(num1,num2)
        elif choice==("3"):
            result==Multiply(num1,num2)
        elif choice==("4"):
            result==Divide(num1,num2)
            print=("Result",result)
        else:
            print("invaild")

calculator()