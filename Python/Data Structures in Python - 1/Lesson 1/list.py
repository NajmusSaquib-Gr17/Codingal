
list1 = ["apple", "banana", "cherry", "date", "grape", 
          "kiwi", "mango", "orange", "strawberry", "watermelon"]

print(list1)
print("Length: ", len(list1))
print(list1[-1])

list1.append("pineapple")
print(list1)

list1.remove("cherry")
print(list1)

list1.sort()
print(list1)

list1.pop(-1)
print(list1)

list1.reverse()
print(list1)

slicedList = list1[2:6]
print(slicedList)

list1.clear()
print(list1)

