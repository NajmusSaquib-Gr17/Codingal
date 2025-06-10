def isNSetBit(num, n):
    if num & (1 << (n-1)):
        print("Set")
    else:
        print("Not Set")

num = int(input("Number: "))
n = int(input("N: "))
isNSetBit(num, n)