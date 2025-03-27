myTuple = (1, 3, 'Hello', 1.5)
print('Tuple: ',myTuple)
emptyTuple = ()
print('Empty Tuple: ',emptyTuple)
nestedTuple = ([1, 2, 3], {'One': 1, 'Two': 2}, (1, 2, 'Hello'))
print('Nested Tuple: ',nestedTuple)
print(type(nestedTuple))
#Tuple data access
print(myTuple[1])
print(nestedTuple[2][2])
#Tuple Slicing
print('Sliced Nested Tuple: ', nestedTuple[0:2])
#Iteration
for i in myTuple:
    print('Hello', i)

for i in nestedTuple:    
    for j in i:
        print('Hello', j)


