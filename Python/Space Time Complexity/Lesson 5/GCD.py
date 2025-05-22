num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

a = num1
b = num2

while b != 0:
    temp = b
    b = a % b
    a = temp

print(f"The GCD of {num1} and {num2} is {a}")