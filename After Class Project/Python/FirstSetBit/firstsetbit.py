def rightmostSetBit(n):
    return n & -n
num = int(input("Enter a Postive Integer Number: "))
print(rightmostSetBit(num))