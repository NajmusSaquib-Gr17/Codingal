def LCM(a, b):
    multiple = max(a, b)
    while True:
        if multiple % a == 0 and multiple % b == 0:
            return multiple
        multiple += 1

x = 12
y = 18
print(f"The LCM of {x} and {y} is: {LCM(x, y)}")