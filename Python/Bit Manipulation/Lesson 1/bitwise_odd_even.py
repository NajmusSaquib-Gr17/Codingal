def isEven(n):
    return(n & 1)==0
num = int(input("Enter any Number: "))

if isEven(num):
    print("Even")
else:
    print("Odd")
    