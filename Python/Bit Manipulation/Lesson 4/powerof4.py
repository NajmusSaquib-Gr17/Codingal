def isPowerOf4(x):
    if x > 0 and (x & (x - 1)) == 0:
        count = 0
        while x > 1:
            x >>= 1
            count += 1
        return (count % 2 == 0) 
    return False


num = []
for i in range(6):
    x = int(input(f"Enter Number {i+1} :"))
    num.append(x)

for x in num:
    if isPowerOf4(x) == True:
        print(x,"is a power of 4")
    else:
        print(x,"is not a power of 4")