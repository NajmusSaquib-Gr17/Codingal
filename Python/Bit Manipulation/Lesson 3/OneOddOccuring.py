def oddOccuring(arr):
    result  = 0
    for element in arr:
        result = result ^ element
    return result

arr = []
n = int(input("Enter array size: "))
for i in range(n):
    num = int(input(f"Enter Element {i+1} :"))
    arr.append(num)
print("Odd Occuring Number: ", oddOccuring(arr))