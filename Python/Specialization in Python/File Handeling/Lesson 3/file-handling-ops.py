with open('Python/Specialization in Python/File Handeling/Lesson 3/Codingal.txt' , 'w') as file :
    file.write('Hi, I am a Coder')
file.close()

with open('Python/Specialization in Python/File Handeling\Lesson 3\Codingal.txt', 'r') as file:
    data = file.readlines()
    print('Printing each words of every line: \n')
    for i in data:
        word = i.split()
        print(word)
        print(type(word))
file.close()