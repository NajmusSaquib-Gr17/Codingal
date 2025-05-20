

number = int(input("Please Enter a Number: "))
sum = 0
var = number



while var > 0 :
    lastDigit = var % 10        
    sum = sum + lastDigit**3    
    var = var // 10             

#If statement for the result output

if sum == number:
    print(number, "is an Armstrong Number")
else:
    print(number, "is not an Armstrong Number") 


