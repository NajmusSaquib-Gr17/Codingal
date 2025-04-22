file1 = open('Python\Specialization in Python\File Handeling\Lesson 2\Codingal.txt', 'r')

file2 = open('Python\Specialization in Python\File Handeling\Lesson 2\Odd_Line.txt', 'w')

content = file1.readlines()
print(type(content))

for line in range(len(content)):
    if (line % 2 ==0):
        file2.write(content[line])

file2.close()

file2 = open('Python\Specialization in Python\File Handeling\Lesson 2\Odd_Line.txt', 'r')
print(file2.read())
file2.close()