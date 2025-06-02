def counter(n):
    counter = 0
    while n:
        counter += 1
        n >>= 1
    return counter
num = int(input())
print(counter(num))

