class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def welcome(self):
        print(f'Hello {self.name}! You are {self.age} years old')

student1 = Student('Najmus Saquib', 20)
student1.welcome()