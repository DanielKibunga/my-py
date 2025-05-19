# class Dog :         ## a method is a function that goes inside a class
     
#     def __init__(self, name , age):
#           self.name = name
#           self.age = age

#     def get_name(self):
#           return self.name
    
#     def get_age (self):
#           return self.age
         
    
#     def set_age(self,age):
#           self.age = age

# d = Dog("Tim", 6)  # we are creating a new instance of the class dog


# d.set_age (11)
# print(d.get_age())



#########students

class Student:
    def __init__(self, name, age, grade):
        self.name = name 
        self.age = age
        self.grade = grade  #0-100

    def get_grade(self):
        return self.grade
    
class Course:

    def __init__(self, name, max_students):
        self.name =name
        self.max_students = max_students
        self.students = []

    def add_student(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True
        return False
    def get_average_grade(self):
        value = 0
        for student in self.students:
            value += student.get_grade()

        return value / len(self.students)
            


s1 = Student("Tim", 18, 80)
s2 = Student("Bella", 19, 98)
s3 = Student("Mill", 17, 70)

course = Course("Science",2)
course.add_student(s1)
course.add_student(s2)
## print(course.students) ## to check whether its working
##print(course.students[1].age) ##to print specifics
print(course.get_average_grade())