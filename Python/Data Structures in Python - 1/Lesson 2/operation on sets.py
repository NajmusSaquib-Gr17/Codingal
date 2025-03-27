mySet = {1, 4, 5, 6, 7, 1, 6, 5, 2, 3, 9, 4}
print(mySet)

fruitsSet = {'Mango', 'Banana', 'Guava', 'Jackfruit', 'Orange', 'Orange', 'Guava'}
print(fruitsSet)

fruitsSet.add('Blackberry')
print(fruitsSet)

numberSet = {1, 3, 5, 7, 9}
print(mySet.difference(numberSet))
print(mySet.symmetric_difference(numberSet))

fruitsSet_2 = {'Mango', 'Blackberry', 'Strawberry', 'Bangi', 'Guava'}
print(fruitsSet.intersection(fruitsSet_2))
print(fruitsSet.union(fruitsSet_2))