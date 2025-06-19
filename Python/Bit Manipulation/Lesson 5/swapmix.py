def swap1(a, b):
    a = (a & b) + (a | b)
    b = a + (~b) + 1
    a = a + (~b) + 1
    print("After Swapping: a = ",a,"b =", b)

print(swap1(56, 12))