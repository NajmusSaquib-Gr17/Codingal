file1 = open('Python/Specialization in Python/File Handeling/Lesson 2/Codingal.txt', 'r')
file2 = open('Python/Specialization in Python/File Handeling/Lesson 2/updatedFile.txt', 'w')

for line in file1.readlines():
    if not (line.startswith('Coding')):
        print(line)

        file2.write

file1.close()
file2.close()