def add(x, y):
    return x + y

def minus(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

num1 = int(input("Enter First Number: "))
num2 = int(input("Enter Second Number: "))
operator = input("Enter the Operation\n1. Addition(+)\n2. Subtraction(-)\n3. Multiplication(*)\n4. Division(/)\n")

if operator == "1":
    print("Result: ", add(num1, num2))
elif operator == "2":
    print("Result: ", minus(num1, num2))
elif operator == "3":
    print("Result: ", multiply(num1, num2))
elif operator == "4":
    if num2 == 0:
        print("Undefined")
    else:
        print("Result: ", divide(num1, num2))
else:
    print("Please Enter a Correct Operator")
