class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, rate):
        if isinstance(lecturer,
                      Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.rates:
                lecturer.rates[course] += [rate]
            else:
                lecturer.rates[course] = [rate]
        else:
            return 'Ошибка'

    def average_score(self):
        middle_sum = 0
        for course_grades in self.grades.values():
            course_sum = 0
            for grade in course_grades:
                course_sum += grade
            middle_of_course = course_sum / len(course_grades)
            middle_sum += middle_of_course
        if middle_sum == 0:
            return f'Студент еще не получал оценки'
        else:
            return f'{middle_sum / len(self.grades.values()):.2f}'

    def __str__(self):
        res = f'Имя: {self.name} \nФамилия: {self.surname} \n'
        res += f'Средняя оценка за домашние задания: {self.average_score()} \n'
        res += f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)} \n'
        res += f'Завершенные курсы: {", ".join(self.finished_courses)}'
        return res


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.rates = {}


class Lecturer(Mentor):
    def middle_rate(self):
        middle_sum: float = 0.0
        for course_grades in self.rates.values():
            course_sum = 0
            for grade in course_grades:
                course_sum += grade
            middle_of_course = course_sum / len(course_grades)
            middle_sum += middle_of_course
        if middle_sum == 0:
            return f'Оценки еще не выставлялись'
        else:
            return f'{middle_sum / len(self.rates.values()):.2f}'

    def __str__(self):
        res = f'Имя: {self.name} \nФамилия: {self.surname}\n'
        res += f'Средняя оценка {self.middle_rate()}\n'
        return res

    def __lt__(self, lecturer):
        if not isinstance(lecturer, Lecturer):
            print(f' Такого лектора нет')
            return
        return self.middle_rate() < lecturer.middle_rate()


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'Имя: {self.name} \nФамилия: {self.surname}\n'
        return res


def grades_students(students_list, course):
    overall_student_rating = 0
    lectors = 0
    for listener in students_list:
        if course in listener.grades.keys():
            average_student_score = 0
            for grades in listener.grades[course]:
                average_student_score += grades
            overall_student_rating = average_student_score / len(listener.grades[course])
            average_student_score += overall_student_rating
            lectors += 1
    if overall_student_rating == 0:
        return f'Оценок по этому предмету нет'
    else:
        return f'{overall_student_rating / lectors:.2f}'


def grades_lecturers(lecturer_list, course):
    average_rating = 0
    b = 0
    for lecturer in lecturer_list:
        if course in lecturer.rates.keys():
            lecturer_average_rates = 0
            for rate in lecturer.rates[course]:
                lecturer_average_rates += rate
            overall_lecturer_average_rates = lecturer_average_rates / len(lecturer.rates[course])
            average_rating += overall_lecturer_average_rates
            b += 1
    if average_rating == 0:
        return f'Оценок по этому предмету нет'
    else:
        return f'{average_rating / b:.2f}'


student_1 = Student('Александр','Сорокин', 'мужской')
student_1.finished_courses = ['Git']
student_1.courses_in_progress = ['Python']

student_2 = Student('Наталья', 'Соловьёва', 'женский')
student_2.finished_courses = ['Git']
student_2.courses_in_progress = ['Python']
students_list = [student_1, student_2]

lecturer_1 = Lecturer('Дмитрий', 'Юдин')
lecturer_1.courses_attached = ['Python', 'Git']

lecturer_2 = Lecturer('Анатолий', 'Шеин')
lecturer_2.courses_attached = ['Python', 'Git']
lecturer_list = [lecturer_1, lecturer_2]

reviewer_1 = Reviewer('Семен', 'Cменов')
reviewer_1.courses_attached = ['Python']

reviewer_2 = Reviewer('Иван', 'Иванов')
reviewer_2.courses_attached = ['Git']

reviewer_1.rate_hw(student_1, 'Git', 8)
reviewer_1.rate_hw(student_1, 'Python', 9)
reviewer_2.rate_hw(student_2, 'Git', 7)
reviewer_2.rate_hw(student_2, 'Python', 8)

student_1.rate_lecturer(lecturer_1, 'Git', 10)
student_2.rate_lecturer(lecturer_2, 'Python', 8)

print(student_1)
print(student_2)
'''
if student_1 > student_2:
    print(f'{student_1.name} учится лучше чем {student_2.name}')
else:
    print(f'{student_2.name} учится лучше чем {student_1.name}')
'''
print(reviewer_1)
print(reviewer_2)

print(lecturer_1)
print(lecturer_2)
'''
if lecturer_1 > lecturer_2:
    print(f'{lecturer_1.name, lecturer_1.surname} преподает лучше чем {lecturer_2.name, lecturer_2.surname}')
else:
    print(f'{lecturer_2.name, lecturer_2.surname} преподает лучше чем {lecturer_1.name, lecturer_1.surname}')
'''
print(f'Средняя оценка студентов по курсу "Git": {grades_students(students_list, "Git")}')
print(f'Средняя оценка студентов по курсу "Python": {grades_students(students_list, "Python")}')

print(f'Средняя оценка лекторов по курсу "Git": {grades_lecturers(lecturer_list, "Git")}')
print(f'Средняя оценка лекторов по курсу "Python": {grades_lecturers(lecturer_list, "Python")}')
