# def LCM(a, b):
#     multiple = max(a, b)
#     while True:
#         if multiple % a == 0 and multiple % b == 0:
#             return multiple
#         multiple += 1

# x = 12
# y = 18
# print(f"The LCM of {x} and {y} is: {LCM(x, y)}")

num1 = 16
num2 = 24

larger = max(num1, num2)
smaller = min(num1, num2)

LCM = int(larger)

while LCM % smaller != 0:
    LCM += larger

print("LCM is:",LCM)