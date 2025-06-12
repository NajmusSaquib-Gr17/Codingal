def twoOddOccurring(arr):
    xor = 0
    for num in arr:
        xor ^= num
    
    setBit = xor & -xor

    x = 0
    y = 0
    for num in arr:
        if num & setBit:
            x ^= num
        else:
            y ^= num

    return x, y

arr = []
n = int(input("Enter array size: "))
for i in range(n):
    num = int(input(f"Enter Element {i+1}: "))
    arr.append(num)
    
odd1, odd2 = twoOddOccurring(arr)
print("Two Odd Occurring Numbers:", odd1, "and", odd2)