my_dict1 = {'name':'Prokhor', 'age': 14}
print(type(my_dict1))

my_dict2 = {'name':'Prokhor', 'age': 14, 'marks':[10, 12, 21]}
my_dict2 = {
    'student1': {
        'name':'John',
        'class': '8'
    },
    'student2': {
        'name':'Billy',
        'class': '8'
    }
}

print(my_dict2)
print(my_dict1['age'])
print(my_dict2.get('student1'))

my_dict2['student3']= {
    'name':'Romelia',
    'class': '8'
}
print(my_dict2)

my_dict2.pop('student3')


my_dict2['student3']= {
    'name':'Romelia',
    'class': '9'
}
print(my_dict2)

my_dict2.clear()
print(my_dict2)