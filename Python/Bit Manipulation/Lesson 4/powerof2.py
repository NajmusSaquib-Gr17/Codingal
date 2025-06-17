def isPowerOfTwo(x):
    if (x==0):
        return False
        
    while(x%2 == 0):
        x /= 2
    return(x==1)


print(isPowerOfTwo(256))
print(isPowerOfTwo(128))
print(isPowerOfTwo(64))
print(isPowerOfTwo(6))
print(isPowerOfTwo(3))
print(isPowerOfTwo(0))