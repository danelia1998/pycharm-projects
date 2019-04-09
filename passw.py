class Student:
    def __init__(self,name,surname,age,average):
        self.name = name
        self.surname = surname
        self.age = age
        self.average = average

    def checker(self):
        if self.average > 92:
            print("student {} have A (GPA)".format(self.name))

student1 = Student("davit","danelia",19,97)
student2 = Student("misha","bagrationi",22,72)
Student.checker(student1)
Student.checker(student2)