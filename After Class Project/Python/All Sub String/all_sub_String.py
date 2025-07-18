def all_substrings(s):
    n = len(s)
    substrings = []
    
    for i in range(n):
        for j in range(i + 1, n + 1):
            substrings.append(s[i:j])
    
    return substrings


text = input("Enter a string: ")
result = all_substrings(text)

print("All substrings:")
for sub in result:
    print(sub)