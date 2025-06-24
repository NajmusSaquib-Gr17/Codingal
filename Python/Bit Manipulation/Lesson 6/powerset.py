import math

def printPowerSet(set, setSize):
    powerSetSize = int(math.pow(2, setSize))
    for i in range(0, powerSetSize):
        for j in range(0, setSize):
            if(i&(1 << j) > 0):
                print(set[j], end=" 3")
        print("")
size = int(input("Enter the size of the set: "))
set = []
for i in range(0, size):
    set.append(int(input("Enter the element: ")))

printPowerSet(set, size)