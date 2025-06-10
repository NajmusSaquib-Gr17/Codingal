def numberOfOnesAndZeros(n):

    ones = 0
    zeros = 0

    while(n):
        if(n&1 == 1):
            ones += 1
        else:
            zeros += 1
        n >>= 1
    print(f"Number of Zeros = {zeros}, Number of Ones = {ones}")

num = int(input("Enter a number: "))
numberOfOnesAndZeros(num)