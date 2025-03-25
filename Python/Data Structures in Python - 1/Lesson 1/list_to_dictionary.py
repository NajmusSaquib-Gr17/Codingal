def listToDict(list):
    result = {}
    for item in list:
        result[item[0]] = item[1:]
    return result

students_data = [
    [101, "Alice Johnson", 20, "A"],
    [102, "Bob Smith", 21, "B"],
    [103, "Charlie Brown", 22, "A"],
    [104, "David Williams", 19, "C"],
    [105, "Emma Davis", 20, "B"]
]

print(students_data)
print(listToDict(students_data))
print(type(listToDict(students_data)))