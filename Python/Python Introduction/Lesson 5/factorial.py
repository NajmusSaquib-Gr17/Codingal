#import sys

#sys.set_int_max_str_digits(10000)

num = int(input("Enter a Number: "))

def factorial(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * factorial(num-1)

if num < 0:
    print("The number must be a positive integer")
else:
    print(f"Factorial of {num} is", factorial(num))