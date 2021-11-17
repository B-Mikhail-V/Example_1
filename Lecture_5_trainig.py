class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)


    def rate_hw(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached \
                and course in self.courses_in_progress and grade in range(1, 11):
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'



class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    # def rate_hw(self, student, course, grade):
    #     if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
    #         if course in student.grades:
    #             student.grades[course] += [grade]
    #         else:
    #             student.grades[course] = [grade]
    #     else:
    #         return 'Ошибка'


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        self.courses_attached = []

    def check_grade(self):
        self.grades in range(1, 11)

    def __str__(self):
        f"{self.check_grade()}"






best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student_2 = Student('Kir', 'Bike', 'your_gender')
best_student.courses_in_progress += ['Python']
best_student_2.courses_in_progress += ['Python']
best_student.courses_in_progress += ['C++']

cool_reviewer = Reviewer('Rev', 'Proff')
cool_reviewer_2 = Reviewer('Rev_2', 'Proff_2')
cool_lecturer = Lecturer('Lec', 'Speaker')
cool_lecturer.courses_attached += ['Python']
cool_lecturer.courses_attached += ['C++']

cool_mentor = Mentor('Some', 'Buddy')
cool_reviewer.courses_attached += ['C++']
cool_reviewer.courses_attached += ['Python']
cool_reviewer_2.courses_attached += ['Python']

best_student.rate_hw(cool_lecturer, 'Python', 5)
best_student_2.rate_hw(cool_lecturer, 'Python', 9)
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student_2, 'Python', 15)
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer_2.rate_hw(best_student_2, 'Python', 25)
# cool_mentor.rate_hw(best_student, 'Python', 10)
# cool_mentor.rate_hw(best_student, 'Python', 10)
# cool_mentor.rate_hw(best_student, 'C++', 10)

a = best_student_2.grades
b = cool_reviewer.courses_attached
c = cool_reviewer.name
d = cool_lecturer.grades
# e = best_student_2.rate_hw(cool_lecturer, 'C++', 20)
print(a)
print(b)
print(c)
print(d)
# print(e)
# print(best_student)
