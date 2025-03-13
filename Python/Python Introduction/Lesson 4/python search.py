array = [4,7,6,8,52,2,5,45,5,8,5,8,5,6,5,65566,5,5844654,456645563,564456,456564,456564546,546,645,564,564,546,564,546,546,2,42,41]

target = int(input("Enter element to find: "))
count = 0
found = False

for i in range(len(array)):
    if array[i] == target:
        found = True #
        count += 1
    #else:
        #index = -1

if found: #index != -1:
    print(f"Element {target} found {count} times")
else:
    print(f"{target} not found")
