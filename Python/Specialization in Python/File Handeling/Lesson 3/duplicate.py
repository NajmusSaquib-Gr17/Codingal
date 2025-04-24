outputFile = open("Python\Specialization in Python\File Handeling\Lesson 3\_testingfile.txt", 'w')

inputFile = open("Python\Specialization in Python\File Handeling\Lesson 3\_new-file.txt", 'r')

line_checked = set()
for line in inputFile:
    if line not in line_checked:
        outputFile.write(line)
        line_checked.add(line)

inputFile.close()
outputFile.close()