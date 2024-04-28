class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

class Teacher(Person):
    def __init__(self, name, age, teacher_id):
        super().__init__(name, age)
        self.teacher_id = teacher_id

# Example usage:
student1 = Student("Alice", 20, "S12345")
print(f"Student Name: {student1.name}, Age: {student1.age}, Student ID: {student1.student_id}")

teacher1 = Teacher("Bob", 35, "T98765")
print(f"Teacher Name: {teacher1.name}, Age: {teacher1.age}, Teacher ID: {teacher1.teacher_id}")
