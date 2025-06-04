def binToDec(n):
    decimal = 0
    power = 0    

    while n > 0:
        lastDigit = n % 10
        decimal += lastDigit * (2 ** power)
        n = n // 10
        power += 1

    return decimal

print(binToDec(11001))

def decToBin(n):
    binary_digit = []

    while n > 0:
        binary_digit.append(str(n % 2))
        n = n // 2
    binary_digit.reverse()

    return "".join(binary_digit) if binary_digit else "0"

print(decToBin(25))