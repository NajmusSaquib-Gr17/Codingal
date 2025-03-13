num = int(input("Enter the numbers: "))
print(f"Table of {num}")

for i in range(1,11):
    sum = num * i
    print(f"{num} * {i} = {sum}")