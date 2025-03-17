#Input from the user

number = int(input("Please Enter a Number to check: "))

#Initial Sum = 0

sum = 0

#Temporary value for while loop

var = number

#While Loop to check the number is Armstrong Number or not

while var > 0 :
    lastDigit = var % 10        #Extracts Last Digit of the Number
    sum = sum + lastDigit**3    #Cube of the Last Digit of the Number
    var = var // 10             #Removes the Last Digit of the Number

#If statement for the result output

if sum == number:
    print(number, "is an Armstrong Number")
else:
    print(number, "is not an Armstrong Number") 


