def is_power_of_8(n):
    if n < 1:
        return False
    while n % 8 == 0:
        n = n // 8
    return n == 1

num = int(input("Enter a number: "))

if is_power_of_8(num):
    print(f"{num} is a power of 8")
else:
    print(f"{num} is not a power of 8")