#Function 1 (1 iteration)
def iteration1 (a, b):    
    return a*b

#Function 2 (N iteration)
def nIteration(a, b):
    if (a>b):
        result = 0
        number1 = b
        for i in range(number1):
            result += a 
        return result 
    else:
        result = 0
        number2 = a
        for i in range(number2):
            result += b 
        return result 
     
    
num1 = 999999999 #int(input("Enter Number 1: "))
num2 = 999999 #int(input("Enter Number 2: "))

#print(iteration1(num1, num2))
print(nIteration(num1, num2))

    