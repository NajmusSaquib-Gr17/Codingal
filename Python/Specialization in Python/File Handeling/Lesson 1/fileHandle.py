file = open('Python\Specialization in Python\File Handeling\Codingal.txt', 'r')
counter = 0

content = file.read()

cd = content.split('\n')

for i in cd:
    if i:
        counter += 1
print(f'Number of Line in the Text = {counter}')
