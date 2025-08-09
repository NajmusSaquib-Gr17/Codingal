import numpy as np

arr = np.array([1, 2, 3, 4, 'abc'])
print(arr)
print(arr[1])
print(arr[2:5])
print(arr.dtype,'\n')




arr = np.array([1, 2, 3, 4], dtype='b')
print(arr)
print(arr.dtype,'\n')




arr = np.array(['3+4j', '5+3j'], dtype='c')
print(arr)
print(arr.dtype,'\n')




arr = np.array([[1,2,3,4],[5,6,7,8]])
print(arr)
print(arr.dtype,'\n')




arr = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
newArr = arr.reshape(4,3)
print(newArr,'\n')
print(arr.dtype,'\n')

for i in arr:
    print(i)
print('\n')

for i in newArr:
    for j in i:
        print(j)
print('\n')






arr1 = np.array([1,2,3,4,5])
arr2 = np.array([6,7,8,9,10])

arrNew = np.concatenate((arr1, arr2))
print(arrNew)
print('\n')

x = np.where(arr == 10)
print(x)
print('\n')



from numpy import random
x1 = random.randint(100)
print(x1)
print('\n')
#np.random.seed()
print(random.randint(1,50, size=5))
print('\n')




arr_1= np.array([5,3,8,6])
arr_sorted = np.sort(arr_1)
print(arr_sorted)
print('\n')



#np.random.seed()
scores= np.random.randint(33, 100, size = (5,3))
print('All Scores \n', scores)
print('Average Score: ', np.mean(scores))
print('Highest Value: ', np.max(scores))
print('Lowest Value: ', np.min(scores))
print('Standard Deviation: ', np.std(scores))

scoreAbove80 = scores[scores >= 80]
print(scoreAbove80)
print(len(scoreAbove80))

bonusScores = np.clip(scores + 5, 38,100)
print(bonusScores)