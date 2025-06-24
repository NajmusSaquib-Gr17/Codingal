def totalFlips(num1, num2):
    flips = 0
    
    while (num1 > 0) or (num2 > 0):
        n1 = (num1 & 1)
        n2 = (num2 & 1)

        if(n1 != n2):
            flips += 1

        num1 >>= 1
        num2 >>= 1

    return flips

num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))

print("The total number of flips needed: ", totalFlips(num1, num2))