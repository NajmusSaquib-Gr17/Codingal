num = int(input("Enter an integer: "))
rev = int(bin(num)[2:][::-1], 2)
print("Reversed bits number:", rev)

