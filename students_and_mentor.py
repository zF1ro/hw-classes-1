class Human:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.grades = {}
    def average_grade(self, grades):
        sum_grades = 0
        len_grades = 0
        for list in grades.values():
            for item in list:
                sum_grades += item
                len_grades += 1
        average_grade = round(sum_grades / len_grades, 2)
        return average_grade

class Student(Human):
    def __init__(self, name, surname, gender):
        super().__init__(name, surname, gender)
        self.finished_courses = []
        self.courses_in_progress = []

    def __str__(self) -> str:
        average_grade = self.average_grade(self.grades)
        #Распаковываем списки
        self_courses_in_progress = ', '.join(self.courses_in_progress)
        self_finished_courses = ', '.join(self.finished_courses)
        printvalue = (f'Студент\nИмя: {self.name}\n'
                    f'Фамилия: {self.surname}\n'
                    f'Пол: {self.gender}\n'
                    f'Средняя оценка за домание задания: {average_grade}\n'
                    f'Курсы в процессе изучения: {self_courses_in_progress}\n'
                    f'Завершенные курсы: {self_finished_courses}')
        return printvalue
    
    def __lt__(self, other):
        if not isinstance(other, Student):
            return 'Not a student'
        return self.average_grade(self.grades) < other.average_grade(other.grades)
    
    def rate_lecture(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if grade in range(1, 11):
                if course in lecturer.grades:
                    lecturer.grades[course] += [grade]
                else:
                    lecturer.grades[course] = [grade]
            else:
                return 'Введено некорректное значение оценки'
        else:
            return 'Ошибка'
        
class Mentor(Human):
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.grades = {}

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
    def __str__(self) -> str:
        #Высчитаем среднюю оценку за все лекции
        average_grade = self.average_grade(self.grades)

        printvalue = (f'Лектор\nИмя: {self.name}\n'
                    f'Фамилия: {self.surname}\n'
                    f'Средняя оценка за лекции: {average_grade}')
        return printvalue
    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            return 'Not a lecturer'
        return self.average_grade(self.grades) < other.average_grade(other.grades)

class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
    def __str__(self) -> str:
        return f'Эксперт, проверяющий домашнее задание\nИмя: {self.name}\nФамилия: {self.surname}'
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if grade in range(1, 11):
                if course in student.grades:
                    student.grades[course] += [grade]
                else:
                    student.grades[course] = [grade]
            else:
                return 'Введено некорректное значение оценки'
        else:
            return 'Ошибка'

#Создаем экземпляры классов
best_student1 = Student('Anton', 'Lutskov', 'male')
best_student1.finished_courses += ['Git', 'Введение в программирование']
best_student1.courses_in_progress += ['Python', 'Data Science']

best_student2 = Student('Vasya', 'Pupkin', 'male')
best_student2.finished_courses += ['Git', 'Введение в программирование']
best_student2.courses_in_progress += ['Python', 'Data Science']

cool_reviewer = Reviewer('Alexandr', 'Bardin')
cool_reviewer.courses_attached += ['Python', 'Data Science']

cool_lecturer1 = Lecturer('Oleg', 'Buligin')
cool_lecturer1.courses_attached += ['Python', 'Data Science']

cool_lecturer2 = Lecturer('Dmitiy', 'Demidov')
cool_lecturer2.courses_attached += ['Python', 'Data Science']

cool_lecturer3 = Lecturer('Elena', 'Nikitina')
cool_lecturer3.courses_attached += ['Python', 'Data Science']

#Используем методы классов
cool_reviewer.rate_hw(best_student1, 'Python', 9)
cool_reviewer.rate_hw(best_student1, 'Python', 9)
cool_reviewer.rate_hw(best_student1, 'Python', 10)

cool_reviewer.rate_hw(best_student1, 'Data Science', 1)
cool_reviewer.rate_hw(best_student1, 'Data Science', 1)
cool_reviewer.rate_hw(best_student1, 'Data Science', 1)

cool_reviewer.rate_hw(best_student2, 'Python', 4)
cool_reviewer.rate_hw(best_student2, 'Python', 5)
cool_reviewer.rate_hw(best_student2, 'Python', 4)

cool_reviewer.rate_hw(best_student2, 'Data Science', 10)
cool_reviewer.rate_hw(best_student2, 'Data Science', 10)
cool_reviewer.rate_hw(best_student2, 'Data Science', 10)

best_student1.rate_lecture(cool_lecturer1, 'Python', 10)
best_student1.rate_lecture(cool_lecturer1, 'Python', 9)
best_student1.rate_lecture(cool_lecturer1, 'Python', 10)

best_student1.rate_lecture(cool_lecturer2, 'Python', 9)
best_student1.rate_lecture(cool_lecturer2, 'Python', 8)
best_student1.rate_lecture(cool_lecturer2, 'Python', 9)

best_student1.rate_lecture(cool_lecturer3, 'Python', 8)
best_student1.rate_lecture(cool_lecturer3, 'Python', 7)
best_student1.rate_lecture(cool_lecturer3, 'Python', 8)

best_student1.rate_lecture(cool_lecturer1, 'Data Science', 10)
best_student1.rate_lecture(cool_lecturer1, 'Data Science', 10)
best_student1.rate_lecture(cool_lecturer1, 'Data Science', 10)

best_student1.rate_lecture(cool_lecturer2, 'Data Science', 7)
best_student1.rate_lecture(cool_lecturer2, 'Data Science', 8)
best_student1.rate_lecture(cool_lecturer2, 'Data Science', 7)

best_student1.rate_lecture(cool_lecturer3, 'Data Science', 8)
best_student1.rate_lecture(cool_lecturer3, 'Data Science', 7)
best_student1.rate_lecture(cool_lecturer3, 'Data Science', 8)

#Выводим результат
print(cool_reviewer, '\n')
print(cool_lecturer1, '\n')
print(cool_lecturer2, '\n')
print(cool_lecturer3, '\n')
print(best_student1, '\n')
print(best_student2, '\n')

#Выводим результаты сравнения
if best_student1 > best_student2:
    print(f'Студент {best_student1.name} имеет среднюю оценку выше, чем студент {best_student2.name}')
else:
    print(f'Студент {best_student2.name} имеет среднюю оценку выше, чем студент {best_student1.name}')
if cool_lecturer1 > cool_lecturer2:
    print(f'Лектор {cool_lecturer1.name} имеет среднюю оценку выше, чем лектор {cool_lecturer2.name}')
else:
    print(f'Лектор {cool_lecturer2.name} имеет среднюю оценку выше, чем лектор {cool_lecturer1.name}')

print()
#Вывод средние оценки студентов и лекторов по курсам
student_list = [best_student1, best_student2]
lecturer_list = [cool_lecturer1, cool_lecturer2, cool_lecturer3]

def average_grade_course_hm(student_list, course):
    sum_grades = 0
    len_grades = 0
    for list in student_list:
        for item in list.grades[course]:
            sum_grades += item
            len_grades += 1
    average_grade = round(sum_grades / len_grades, 2)
    return average_grade

def average_grade_lecturer(lecturer_list, course):
    sum_grades = 0
    len_grades = 0
    for list in lecturer_list:
        for item in list.grades[course]:
            sum_grades += item
            len_grades += 1
    average_grade = round(sum_grades / len_grades, 2)
    return average_grade

print('Средняя оценка по курсу Data Science: ', average_grade_course_hm(student_list, 'Data Science'))
print('Средняя оценка по курсу Python: ', average_grade_course_hm(student_list, 'Python'))

print('Средняя оценка по лектору Python: ', average_grade_lecturer(lecturer_list, 'Python'))
print('Средняя оценка по лектору Data Science: ', average_grade_lecturer(lecturer_list, 'Data Science'))