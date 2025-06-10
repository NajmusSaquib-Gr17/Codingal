def firstBitSet(n):
    count=1

    while(n):
        if(n&1==1):
            break
        count+=1
        n>>=1
    return count
num = int(input("Enter a number: "))
print("The frist set bit is at position", firstBitSet(num))
