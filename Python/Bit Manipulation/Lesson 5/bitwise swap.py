def swap1(a, b):
    a = a ^ b
    b = a ^ b
    a = a ^ b
    print("After Swapping: a = ",a,"b =", b)

print(swap1(56, 12))