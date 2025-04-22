file = open('Python\Specialization in Python\File Handeling\Lesson 2\Codingal.txt', 'r')
print(file.read())
file.close()

file = open('Python\Specialization in Python\File Handeling\Lesson 2\Codingal.txt', 'r')
print('\nFirst 8 Character on the file')
print(file.read(8))
file.close()

file = open('Python\Specialization in Python\File Handeling\Lesson 2\Codingal.txt', 'a')
file.write('\nHi! My name is Najmus Saquib')
file.write('\nThis is a new line added to the file')
file.close()

file = open('Python\Specialization in Python\File Handeling\Lesson 2\Codingal.txt', 'r')
print(file.read())
file.close()