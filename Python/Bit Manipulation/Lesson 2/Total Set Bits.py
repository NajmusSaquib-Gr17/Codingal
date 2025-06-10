def totalSetBits(n):
    count = 0

    while(n):
        if(n&1 == 1):
            count += 1
        n >>= 1
    return count

num = int(input("Enter a number: "))
print("Total Set Bits", totalSetBits(num))